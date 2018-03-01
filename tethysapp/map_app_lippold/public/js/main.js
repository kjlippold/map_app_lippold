require([
  "esri/Map",
  "esri/layers/FeatureLayer",
  "esri/layers/MapImageLayer",
  "esri/views/MapView",
  "dojo/dom",  
  "dojo/on",   
  "dojo/domReady!"
], 
function(Map, FeatureLayer, MapImageLayer, MapView, dom, on){

  var map = new Map({
    basemap: "hybrid"
  });

  var template = {
    title: "County Name:",
    content: "<p>{NAME}</p>"
  };
  
  var utah_dem_layer = new MapImageLayer({
    url:"http://geoserver2.byu.edu/arcgis/rest/services/PawneeRangers/DEM/MapServer",
    id:"dem"
  });

  var utah_mun_layer = new FeatureLayer({
    url:"http://geoserver2.byu.edu/arcgis/rest/services/PawneeRangers/Municipalities/MapServer",
    id:"municipalities",
    outFields: ["*"],
    popupTemplate:template
  });

  map.layers.add(utah_dem_layer)
  map.layers.add(utah_mun_layer)

  var view = new MapView({
    container: "viewDiv",
    map: map, 
    zoom: 8,  
    center: [-111, 40]  
  });
  var demlayer = dom.byId("dem");
  on(demlayer, "change", function(){
    utah_dem_layer.visible = demlayer.checked;
  });
  
  var municipalitieslayer = dom.byId("municipalities");

  on(municipalitieslayer, "change", function(){
    utah_mun_layer.visible = municipalitieslayer.checked;
  });

});
