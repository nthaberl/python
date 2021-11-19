//Initialize map, pulling in map id from div
var map = L.map('map').setView([47.5962, -120.6615], 7);

//base tile
var tile = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

tile.addTo(map)

//Terrain Map Tile from Google
var googleTerrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',{ //"p" in URL indicates terrain map
maxZoom: 20,
subdomains:['mt0','mt1','mt2','mt3']
});

googleTerrain.addTo(map)


//Pulling data from SQL and dynamically adding it to map
function getTrails() {
    fetch("http://localhost:5000/api/trails")
    .then(response => response.json())
    .then(data => {
        //adding new markers based on coordinates
        for (var i = 0; i < data.length; i++){
            var newMarker = L.marker([data[i].lat, data[i].lng]).bindPopup(data[i].name + " - " + data[i].description);
            newMarker.addTo(map);
        }
        var trailTable = document.querySelector("#trails")
        trailTable.innerHTML = "";

        //adding Name data to table
        for (var i=0; i < data.length; i++){
            console.log(data[i].name)
            let row = document.createElement("tr")
            let name = document.createElement("td");
            name.innerHTML = data[i].name
            row.appendChild(name)
            trailTable.appendChild(row)
        }
    })
}

getTrails();


//HANDLING THE SUBMIT FORM
let name = ""
let description = ""
let lat = 0
let lng = 0

function setName(element){
    name = element.value;
}

function setDescription(element){
    description = element.value;
}

function setLat(element){
    lat = element.value;
}

function setLong(element){
    lng = element.value;
}

function handleSubmit(){
    const options = {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
    body: JSON.stringify({
        name: name,
        description: description,
        lat: lat,
        lng: lng,
    })
    }
    
    fetch("http://localhost:5000/api/trails/create", options)
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    getTrails(); //recalls the function to refresh the info on the page!
    document.querySelector("#name").value = "";
    document.querySelector("#description").value = "";
    document.querySelector("#lat").value = "";
    document.querySelector("#lng").value = "";
}