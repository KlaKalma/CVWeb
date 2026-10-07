let modeindivSB = false;

let nbcases = [5,15]; // lignes , colones mais avec les infos

let margetext = 9;
let marges = 50; // marges pour les bords du SB

let affichagesmulti = [["Index","Coords","Fitness","Stamina","ID"],["Index","Coords","Fitness","Séléctions","Tmp de Vie"]];
let naffichagemulti = 0;
let nomsSB = affichagesmulti[naffichagemulti];

let modeaffichage = [1,2,3];
let lmodeaffichage = [[1,2,3],[1,4,5]];
let nmodeaffichage = 0;

let modetri = 3; // Fitness , ID , Stamina,"Séléctions"

let espacementX,espacementY;
let populationaffichage;

let ordretricroissant = false;

function calcSB(individu,population){
	
	if(modeindivSB == true){
		affichernodes(individu);
	} else {
		afficheSBmulti(individu,population);
	}

	textSize(30);
	fill(255);
	textAlign(CENTER);
	text("Renaissances : " + nguerrier + " Ratio : " + floor(ratioséléc * 100000)/100000 , TX + TXX / 2, marges - margetext);
}

// nb cases lignes colones

function afficheSBmulti(individu,population){

	strokeWeight(3);

	espacementX = ((TX - 2 * marges) / nbcases[0]);
	espacementY = ((TY - 2 * marges) / nbcases[1]);

	for(let i = 0; i <= nbcases[1];i++){ // horizontales
		line(TX + marges, marges + i * espacementY,TX + TXX - marges, marges + i * espacementY);
	}

	for(let i = 0; i <= nbcases[0];i++){ // verticales
		line(TX + marges + i * espacementX,marges,TX + marges + i * espacementX, TY - marges);
	}

	line(TX + marges + 1.5 * espacementX,marges + espacementY,TX + marges + 1.5 * espacementX, TY - marges); // séparation coords

	textSize(30);
	fill(255);
	textAlign(CENTER);
	strokeWeight(1);

	for(let i = 0; i < nbcases[0];i++){ // affichage noms en haut + triangle tri
		text(nomsSB[i],TX + marges + (i + 0.5) * espacementX,marges + margetext + 0.5 * espacementY)
		if(modeaffichage[i-2] == modetri){
			if(ordretricroissant == true){
				fill(0,255,0);
			}else{
				fill(255,0,0);
			}

			triangle(TX + marges + (i + 0.5) * espacementX - 10,marges,TX + marges + (i + 0.5) * espacementX + 10,marges,TX + marges + (i + 0.5) * espacementX,marges + 10);
			fill(255);
		}
	}

	populationaffichage = triage(population,modetri);
	
	for(let i = 0; i < nbcases[1] - 1 && i < populationaffichage.length; i++){
		if(populationaffichage[i][0] == indexexposé[0] && populationaffichage[i][1] == indexexposé[1]){
			fill(255,255,0)
		} else {
			fill(couleurpopu[populationaffichage[i][0]][0],couleurpopu[populationaffichage[i][0]][1],couleurpopu[populationaffichage[i][0]][2])
		}
		text(populationaffichage[i][0] + " | " + populationaffichage[i][1],TX + marges + 0.5 * espacementX, margetext + marges + (1.5 + i) * espacementY);
		text(floor(population[populationaffichage[i][0]][populationaffichage[i][1]].coords.x),TX + marges + 1.25 * espacementX, margetext + marges + (1.5 + i) * espacementY);
		text(floor(population[populationaffichage[i][0]][populationaffichage[i][1]].coords.y),TX + marges + 1.75 * espacementX, margetext + marges + (1.5 + i) * espacementY);
		text(floor(valeur(modeaffichage[0],population[populationaffichage[i][0]][populationaffichage[i][1]])),TX + marges + 2.5 * espacementX, margetext + marges + (1.5 + i) * espacementY);
		text(floor(valeur(modeaffichage[1],population[populationaffichage[i][0]][populationaffichage[i][1]])),TX + marges + 3.5 * espacementX, margetext + marges + (1.5 + i) * espacementY);
		text(floor(valeur(modeaffichage[2],population[populationaffichage[i][0]][populationaffichage[i][1]])),TX + marges + 4.5 * espacementX, margetext + marges + (1.5 + i) * espacementY);
	}
	
}

function triage(population,type){
	let triés = [];

	triés.push([0,0]);

	for(let i = 0; i < population.length;i++){
		let temp;
		if(i == 0)temp = 1
		else temp = 0
		for(let j = temp; j < population[i].length;j++){
			if(valeur(type,population[i][j]) <= valeur(type,population[triés[triés.length - 1][0]][triés[triés.length - 1][1]]) && ordretricroissant == false){
				triés.push([i,j]);
			}else if(ordretricroissant == false){
				for(let k = 0;k < triés.length;k++){
					if(valeur(type,population[i][j]) > valeur(type,population[triés[k][0]][triés[k][1]])){
						triés.splice(k, 0, [i,j]);
						break;
					}
				}
			//croissant
			}else if(valeur(type,population[i][j]) >= valeur(type,population[triés[triés.length - 1][0]][triés[triés.length - 1][1]]) && ordretricroissant == true){
				triés.push([i,j]);
			}else if(ordretricroissant == true){
				for(let k = 0;k < triés.length;k++){
					if(valeur(type,population[i][j]) < valeur(type,population[triés[k][0]][triés[k][1]])){ // valeur qu'on vetu mettre < valeur qu'il compare
						triés.splice(k, 0, [i,j]);
						break;
					}
				}
			}
		}
	}
	return triés

}

function valeur(type,individu){
	if(type === 1){
		let temp = individu.calcFitness();
		return temp
	} else if (type === 3){
		return individu.id
	}else if (type === 2){
		return individu.stamina
	}else if (type === 4){
		return individu.nbséléctions
	} else if (type === 5){
		return individu.tmpsdevie
	}
}

function switchordretri(){
	if(ordretricroissant == true){
		ordretricroissant = false;
	} else {
		ordretricroissant = true;
	}
}

function changeaffichage (){
	naffichagemulti ++;
	naffichagemulti = naffichagemulti % affichagesmulti.length;

	nomsSB = affichagesmulti[naffichagemulti];

	nmodeaffichage ++;
	nmodeaffichage = nmodeaffichage % lmodeaffichage.length;

	modeaffichage = lmodeaffichage[nmodeaffichage];

}

let affichernodes = (individu) => {
	
	for (let i = 0; i < individu.ADN.neurones.length; i++) {
		X = TXX / (individu.ADN.neurones.length + 1) * ( i + 1 );
		for(let j = 0; j < individu.ADN.neurones[i].length;j++){

			Y = TY / (individu.ADN.neurones[i].length + 1) * ( j + 1 );

			colorMode(HSB);

			for(let k = 0;k < individu.ADN.neurones[i][j].connections.length;k++){
				Ynode = TY / (individu.ADN.neurones[i][j].connections.length + 1) * ( k + 1 );
				Xnode = TXX / (individu.ADN.neurones.length + 1) * ( i + 2 );

				let couleurliaison, poids;

				if(individu.ADN.neurones[i][j].valeur * individu.ADN.neurones[i][j].connections[k] < 0){ //rouge
					couleurliaison = [360,100,individu.ADN.neurones[i][j].valeur * individu.ADN.neurones[i][j].connections[k] * -100];
					poids = floor(individu.ADN.neurones[i][j].valeur * individu.ADN.neurones[i][j].valeur * 5);
				} else { // vert
					couleurliaison = [120,100,individu.ADN.neurones[i][j].valeur * individu.ADN.neurones[i][j].connections[k] * 100];
					poids = ceil(individu.ADN.neurones[i][j].connections[k] * individu.ADN.neurones[i][j].valeur* 5);
				}

				strokeWeight(poids);

				stroke(couleurliaison[0],couleurliaison[1],couleurliaison[2]);

				line(X + TXX,Y,TXX + Xnode,Ynode);

			}

			let couleurrond;

			if(individu.ADN.neurones[i][j].valeur < 0){ //rouge
				couleurrond = [360,100,individu.ADN.neurones[i][j].valeur * -100];
			} else { // vert
				couleurrond = [120,100,individu.ADN.neurones[i][j].valeur * 100];
			}

			strokeWeight(1);
			stroke(255);
			fill(couleurrond[0],couleurrond[1],couleurrond[2]);
			ellipse(X + TXX,Y,50);
		}
	}

	colorMode(RGB);

	textSize(30);
	fill(255);
	textAlign(RIGHT);

	for(let j = 0; j < individu.ADN.neurones[0].length;j++){
		text(individu.ADN.neurones[0][j].name,TX + TXX / (individu.ADN.neurones.length + 1) - 30,TY / (individu.ADN.neurones[0].length + 1) * ( j + 1 ) + 10)
	}
	textAlign(LEFT);
	for(let j = 0; j < individu.ADN.neurones[individu.ADN.nbneurones.length - 1].length;j++){
		text(individu.ADN.neurones[individu.ADN.nbneurones.length - 1][j].name,TX + TXX - TXX / (individu.ADN.neurones.length + 1) + 30,TY / (individu.ADN.neurones[individu.ADN.nbneurones.length - 1].length + 1) * ( j + 1 ) + 10)
	}

	let texteinfos = [["Stamina",floor(individu.stamina)],["Id",individu.id]];

	textAlign(CENTER);

	for (let i = 0; i < texteinfos.length; i++) {
		let X = TX + TXX * (i+1) / (texteinfos.length + 1);
		let Y = TY - 30;

		text(texteinfos[i][0] + " : " + texteinfos[i][1],X,Y);
	}

}