let TX = 900; // window.innerWidthwindow.innerHeight
let TXX = 900;
let TY = 900;

const E = Math.E;
let trace = false;

let couleurpopu = [[0,255,0],[255,0,0],[0,0,255]];
let couleurexposé = [255,255,0];

let guerriers = [];
let points = [];
let nbpopus = 3;

let nbpointsdépart = 15;
let probaboufe = 2/3;

let débuggage = [];

let lstatistiques = [];
let moyennestat = 0;
let sommestat, ratioséléc;

let indexexposé = [0,0];

let modetest = false;

let exposé;

function setup() {
	
	createCanvas(TX + TXX, TY);
	background(0);
	stroke(250);

	for(let i = 0; i < nbpopus; i++){
		points.push([]);
		popu.push([]);
		for(let j = 0; j < taillepopudépart;j++){
			popu[i].push(new guerrier(i));
		}
	}

	if(modetest != true){
		for(let i = 0;i < nbpointsdépart;i++){
			nouveaupoint();
		}
	} else {
		for(let i = 0; i < nbpopus * 2;i++){
			nouveaupoint();
		}
	}
}

function draw() {

	exposé = popu[indexexposé[0]][indexexposé[1]];

	if(trace != true){
		background(0);
	}

	line(TX,0,TX,TY);

	let vie = 0;

	exposé.couleur = [couleurexposé[0],couleurexposé[1],couleurexposé[2]];

	for(let i = 0; i < popu.length;i++){
		let boufes = [];
		let poisons = [];

		for(let j = 0;j < i;j++){
			poisons = poisons.concat(points[j]);
		}
		for(let j = i + 1;j < points.length;j++){
			poisons = poisons.concat(points[j]);
		}

		boufes = points[i];

		for(let j = 0;j < popu[i].length;j++){
			popu[i][j].update(boufes,poisons);

			let afficherpointsproche;

			if(indexexposé[0] == i && indexexposé[1] == j) afficherpointsproche = true;
			else afficherpointsproche = false;

			if(popu[i][j].estvivant() == false){
				mort([i,j],popu);
			} else {
				popu[i][j].show(afficherpointsproche);
			}
		}
	}

	calcSB(exposé,popu);

	for(let i = 0;i < points.length;i++){
		for(let j = 0;j < points[i].length;j++){
			points[i][j].show(i);
		}
	}
}

function keyPressed() {
	if (key == "S") {
		saveJSON(popu[indexexposé[0]][indexexposé[1]].ADN, 'ADNindividu.json');
	}else if(key == "T"){
		if(modeindivSB == true){
			modeindivSB = false;
		}else {
			modeindivSB = true;
		}
	} else if(key == "C"){
		if(modeindivSB == false){
			changeaffichage();
		}
	}
}

function mousePressed(){
	if(mouseX < TX){
		exposé.couleur = couleurpopu[exposé.npopu];

		for(let i = 0; i < popu.length;i++){
			for(let j = 0; j < popu[i].length;j++){
				if(dist2(popu[indexexposé[0]][indexexposé[1]].coords.x,popu[indexexposé[0]][indexexposé[1]].coords.y,mouseX,mouseY) > dist2(popu[i][j].coords.x,popu[i][j].coords.y,mouseX,mouseY)){
					indexexposé = [i,j];
				}
			}
		}

	}else { // sur le score board
		if(modeindivSB == false){
			if(mouseX > TX + marges && mouseX < TX + TXX - marges && mouseY > marges + espacementY && mouseY < TY - marges){
				exposé.couleur = couleurpopu[exposé.npopu];
				indexexposé = populationaffichage[floor((mouseY - marges) / espacementY) - 1];
			} else if(mouseX > TX + marges + 2*espacementX && mouseX < TX + TXX - marges - 2*espacementX && mouseY > marges && mouseY < marges + espacementY){
				if(modetri == modeaffichage[0]){
					switchordretri();
				} else {
					modetri = modeaffichage[0]; // Fitness , ID , Stamina
				}
			} else if(mouseX > TX + marges + 3*espacementX && mouseX < TX + TXX - marges - 1*espacementX && mouseY > marges && mouseY < marges + espacementY){
				if(modetri == modeaffichage[1]){
					switchordretri();
				} else {
					modetri = modeaffichage[1]; // Fitness , ID , Stamina
				}
				
			}else if(mouseX > TX + marges + 4*espacementX && mouseX < TX + TXX - marges && mouseY > marges && mouseY < marges + espacementY){
				if(modetri == modeaffichage[2]){
					switchordretri();
				} else {
					modetri = modeaffichage[2]; // Fitness , ID , Stamina
				}
			}
		}
	}
}

function calce(x){
	return 2/(1+(E**(-x))) - 1
}

function calcmoydist(x){
	if(x < (TX + TY)/2){
		return	(x/((TX+TY)/2))
	} else {
		return 1
	}
}

function dist2(x1,y1,x2,y2) {
	distance = (y1 - y2)**2 + (x1 - x2)**2;
	return distance
}

let nouveaupoint = () => { // nouvelle manière décrire une fonction
	
	let fait = false;

	for(let i = 0;i < points.length;i++){
		if(points[i].length == 0){
			points[i].push(new Pt());
			fait = true;
			break;
		}
	}
	if(fait == false){
		points[floor(random() * nbpopus)].push(new Pt());
	}
}

function suprimerpoint(point){

	for(let i = 0; i < points.length;i++){
		for(let j = 0;j < points[i].length;j++){
			if(points[i][j] == point){
				points[i].splice(j,1);
			}
		}
	}
	nouveaupoint();
}

function ajouteruneséléction(index){
	listeindexstat.push(index);
	popu[index[0]][index[1]].nbséléctions ++;
	lstatistiques.push(popu[index[0]][index[1]].calcFitness());
	if(lstatistiques.length >= 50) lstatistiques.splice(0,lstatistiques.length - 50);
	sommestat = 0;
	for(let i = 0; i < lstatistiques.length;i++){
		sommestat += lstatistiques[i];
	}
	sommestat /= lstatistiques.length;
	ratioséléc = 0;
	let sommepopu, taillepopu;
	sommepopu = 0;
	taillepopu = 0;
	for(let i = 0;i < popu.length;i++){
		for(let j = 0; j < popu[i].length;j++){
			sommepopu += popu[i][j].calcFitness();
			taillepopu ++;
		}
	}

	sommepopu = sommepopu / taillepopu;
	ratioséléc = sommestat / sommepopu;
	
}
