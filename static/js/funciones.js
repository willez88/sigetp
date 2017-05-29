/**
 * @brief Función que muestra una ventana emergente con un mapa para la selección de las coordenadas geográficas
 * @param title Titulo de la ventana emergente
 * @param template Plantilla html a utilizar para mostrar el formulario
 */
function seleccionar_coordenadas(title, template) {
    var modal = bootbox.dialog({
        title: title,
        message: template,
        buttons: {
            success: {
                label: BTN_AGREGAR,
                className: "btn btn-default btn-sm",
                callback: function() {
                    $("#id_coordenada_0").val($(modal).find("#inputLongitud").val());
                    $("#id_coordenada_1").val($(modal).find("#inputLatitud").val());
                }
            },
            main: {
                label: BTN_CANCELAR,
                className: "btn btn-default btn-sm"
            }
        },
        show: false //Por defecto no se muestra la ventana modal al invocarla para poder cargar el mapa
    });
    $(modal).on("shown.bs.modal", function() {
        /* Carga el mapa cuando la ventana modal es mostrada */
        load_map();
    });
    /* Muestra la ventana de dialogo modal despues de haber cargado el mapa en su correspondiente div */
    $(modal).modal("show");
}

/**
 * @brief Función que carga los datos del mapa a mostrar para la selección de coordenadas geográficas
 */
function load_map() {
    $(document).ready(function() {
        var app = {};

        /**
         * @constructor
         * @extends {ol.interaction.Pointer}
         */
        app.Drag = function() {
            ol.interaction.Pointer.call(this, {
                handleDownEvent: app.Drag.prototype.handleDownEvent,
                handleDragEvent: app.Drag.prototype.handleDragEvent,
                handleMoveEvent: app.Drag.prototype.handleMoveEvent,
                handleUpEvent: app.Drag.prototype.handleUpEvent
            });

            /**
             * @type {ol.Pixel}
             * @private
             */
            this.coordinate_ = null;

            /**
             * @type {string|undefined}
             * @private
             */
            this.cursor_ = 'pointer';

            /**
             * @type {ol.Feature}
             * @private
             */
            this.feature_ = null;

            /**
             * @type {string|undefined}
             * @private
             */
            this.previousCursor_ = undefined;
        };

        ol.inherits(app.Drag, ol.interaction.Pointer);

        /**
         * @param {ol.MapBrowserEvent} evt Map browser event.
         * @return {boolean} `true` to start the drag sequence.
         */
        app.Drag.prototype.handleDownEvent = function(evt) {
            var map = evt.map;

            var feature = map.forEachFeatureAtPixel(evt.pixel, function(feature) {
                return feature;
            });

            if (feature) {
                this.coordinate_ = evt.coordinate;
                this.feature_ = feature;
            }

            return !!feature;
        };

        /**
         * @param {ol.MapBrowserEvent} evt Map browser event.
         */
        app.Drag.prototype.handleDragEvent = function(evt) {
            var deltaX = evt.coordinate[0] - this.coordinate_[0];
            var deltaY = evt.coordinate[1] - this.coordinate_[1];

            var geometry = (this.feature_.getGeometry());
            geometry.translate(deltaX, deltaY);
            $("#inputLongitud").val(evt.coordinate[0]);
            $("#inputLatitud").val(evt.coordinate[1]);

            this.coordinate_[0] = evt.coordinate[0];
            this.coordinate_[1] = evt.coordinate[1];
        };

        /**
         * @param {ol.MapBrowserEvent} evt Event.
         */
        app.Drag.prototype.handleMoveEvent = function(evt) {
            if (this.cursor_) {
                var map = evt.map;
                var feature = map.forEachFeatureAtPixel(evt.pixel, function(feature) {
                    return feature;
                });
                var element = evt.map.getTargetElement();

                if (feature) {
                    if (element.style.cursor != this.cursor_) {
                        this.previousCursor_ = element.style.cursor;
                        element.style.cursor = this.cursor_;
                    }
                } else if (this.previousCursor_ !== undefined) {
                    element.style.cursor = this.previousCursor_;
                    this.previousCursor_ = undefined;
                }
            }
        };

        /**
         * @return {boolean} `false` to stop the drag sequence.
         */
        app.Drag.prototype.handleUpEvent = function() {
            this.coordinate_ = null;
            this.feature_ = null;
            return false;
        };

        var satellite = new ol.layer.Tile({
            source: new ol.source.MapQuest({layer: 'sat'})
        });

        var osm = new ol.layer.Tile({
            source: new ol.source.OSM()
        });

        var iconGeometry = new ol.geom.Point([-65.0000,6.5000]).transform('EPSG:4326', 'EPSG:3857');

        var pointFeature = new ol.Feature({
            geometry: iconGeometry,
            name: 'Mark'
        });

        var iconStyle = new ol.style.Style({
            image: new ol.style.Icon(({
                anchor: [0.5, 15], // Posicion del icono en el eje X Y
                anchorXUnits: 'fraction', // Unidad de medida para el posicionamiento del icon en el eje X
                anchorYUnits: 'pixels', // Unidad de medida para el posicionamiento del icon en el eje X
                //opacity: 0.75,
                src: URL_STATIC_FILES+'img/mark.png',
                // the scale factor
                scale: 1.1 // Tamaño de la imagen de acuerdo a la escala en base al tamaño original
            }))
        });

        pointFeature.setStyle(iconStyle);

        var vectorLayer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: [pointFeature]
            })
        });

        var map = new ol.Map({
            interactions: ol.interaction.defaults().extend([new app.Drag()]),
            target: 'map',
            layers: [osm, vectorLayer],
            view: new ol.View({
                center: ol.proj.transform([-65.0000,6.5000], 'EPSG:4326', 'EPSG:3857'),
                zoom: 4
            })
       });

        var mousePosition = new ol.control.MousePosition({
            coordinateFormat: ol.coordinate.createStringXY(6),
            projection: 'EPSG:3857',
            target: document.getElementById('myposition'),
            undefinedHTML: '&nbsp;'
        });

        map.on('singleclick', function(evt) {
            $("#inputLongitud").val(evt.coordinate[0]);
            $("#inputLatitud").val(evt.coordinate[1]);
            // Modifica la posición actual del marcador al hacer click sobre un punto en el mapa
            iconGeometry.setCoordinates(evt.coordinate);
            //console.log(evt.pixel);
        });

        map.addControl(mousePosition);

        map.on('loadstart', function() {
            cargando.showPleaseWait();
        });

        map.on('loadend', function() {
            cargando.hidePleaseWait();
        });

        map.updateSize();
    });
}
