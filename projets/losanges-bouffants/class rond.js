let taillebase = 5; // angle en radians
let taillenavette = 15; // hauteur  
let écartnode = 10;

let nguerrier = 0; // num guerrier
let affichenode = false;

if(modetest == true){
	affichenode = true;
}

let strafeactivé = true;

class guerrier{
	constructor(npopu,x,y,or){

		if(x && y){
			this.coords = createVector(x,y);
		}else {
			this.coords = createVector(random(TX),random(TY));
		}
		this.vitesse = createVector(0, 0);
		this.acc = createVector(0, 0);
		if(or){
			this.or = or;
		} else {
			this.or = random(0, TWO_PI);
		}
		this.Bproche = 0;
		this.Pproche = 0;

		this.npopu = npopu;

		this.vitessemax = 4;
		this.accmax = 2;

		this.fitness = 0;
		this.fitnessrégulée = 0;

		this.stamina = 250;
		this.staminamax = this.stamina;

		this.tmpsdevie = 0;

		this.nbboufemangé = 0;
		this.nbpoisonmangé = 0;

		this.nbséléctions = 0;

		this.couleur = couleurpopu[this.npopu];

		this.id = nguerrier;
		nguerrier++;
		
		class ADN{
			constructor(){
				class neurone{ // class neurones
					constructor(avant,apres){
						this.valeur = 0; //valeur pdt les calculs
						this.nbavant = avant; // nb de neurones colone avant
						this.nbapres = apres; // nb neurones apres
						this.name = ""; // nom des neurones
						this.connections = []; // connections avec les neurones apres 
						for(let i = 0;i < this.nbapres;i++){
							this.connections.push(random(-1,1)); // pour chauque neurones apres crées une connection
						}
					}
				}

				this.neurones = []; // liste des neurones
				
				this.nbneurones = [9,6,6,3]; // nb de neurones de chaques catégories

				this.nomentrées = ["Velocité","Node G B","Node D B","Or B","DistB","Node G P","Node D P","Or P","DistP"];
				this.nomsorties = ["Rotation","Avance","Strafe"];

				for(let i = 0; i < this.nbneurones.length; i++){
					this.temp = [];

					let nbavant,nbapres

					if(i == 0){
						nbavant = 0
						nbapres = this.nbneurones[i+1];
					} else if (i == this.nbneurones.length - 1){
						nbavant = this.nbneurones[i-1];
						nbapres = 0;
					} else {
						nbavant = this.nbneurones[i - 1];
						nbapres = this.nbneurones[i + 1];
					}

					for(let j = 0;j < this.nbneurones[i];j++){
						this.temp.push(new neurone(nbavant,nbapres));
						if(i == 0){
							this.temp[j].name = this.nomentrées[j];
						} else if(i == this.nbneurones.length - 1){
							this.temp[j].name = this.nomsorties[j];
						}
					}
					this.neurones.push(this.temp);
				}
			}
		}

		this.ADN = new ADN();

	}

	update(listeB,listeP){ // la fontion qui pique +++++++++++++++++++++++++++++++++++++++++++++++++++++

		this.fitness = this.calcFitness(); 

		this.Bproche = this.calcProche(listeB);

		this.Pproche = this.calcProche(listeP);

		this.temp = [listeB[this.Bproche],listeP[this.Pproche]];

		this.calcentrée(listeB,listeP);

		this.calccachés();

		this.calcsorties();

		this.calcstamina(listeB,listeP);

		this.calcphysique();

		this.tmpsdevie += 1;

	}

	calccolisions(){
		if(this.coords.x < 0){
			this.vitesse.x = abs(this.vitesse.x);
		} else if(this.coords.x > TX){
			this.vitesse.x = -abs(this.vitesse.x);
		}

		if(this.coords.y < 0){
			this.vitesse.y = abs(this.vitesse.y);
		} else if(this.coords.y > TY){
			this.vitesse.y = -abs(this.vitesse.y);
		}
	}

	ajouterforce(force){
		this.acc.add(force);
	}

	estvivant(){
		if(this.stamina > 0){
			return true
		} else {
			return false
		}
	}

	calcsorties(listeB,listeP){
		// sorties 

		//rotation

		this.rotation = this.ADN.neurones[this.ADN.neurones.length - 1][0].valeur / 4;
		this.or += this.rotation;

		// avancement
		this.avance = createVector(-cos(this.or),-sin(this.or));
		this.avance.setMag(this.ADN.neurones[this.ADN.neurones.length - 1][1].valeur);
		this.ajouterforce(this.avance);

		if(strafeactivé == true){
			// strafe
			this.strafe = createVector(cos(this.or - HALF_PI),sin(this.or - HALF_PI));
			this.strafe.setMag(this.ADN.neurones[this.ADN.neurones.length - 1][2].valeur / 10);
			this.ajouterforce(this.strafe);
		}
	}

	calcentrée(listeB,listeP){

		let Boufe,Poison;

		//vitesse
		if(this.ADN.nbneurones[0] >= 1){
			this.ADN.neurones[0][0].valeur = calce(this.vitesse.mag());
		}

		// 2 neurones ( 2 nodes ) 

		if(this.ADN.nbneurones[0] >= 3){
			this.Bproche = this.calcProche(listeB);

			Boufe = listeB[this.Bproche];

			this.nodeprocheboufe = this.calccoordsnode(Boufe);

			if(this.nodeprocheboufe == "O"){
				this.ADN.neurones[0][1].valeur = -1;
				this.ADN.neurones[0][2].valeur = 1;
			} else {
				this.ADN.neurones[0][1].valeur = 1;
				this.ADN.neurones[0][2].valeur = -1;
			}
		}

		//distance boufe plus proche

		if(this.ADN.nbneurones[0] >= 4){

			this.corpsnodeboufe = this.calcrapportdist(Boufe);

			if(this.corpsnodeboufe == "N"){
				this.ADN.neurones[0][3].valeur = -1;
			} else {
				this.ADN.neurones[0][3].valeur = 1;
			}
		}

		// distance boufe plus proche

		if(this.ADN.nbneurones[0] >= 5)this.ADN.neurones[0][4].valeur = calcmoydist(dist(this.coords.x,this.coords.y,Boufe.x,Boufe.y));

		//or poison plus proche sert a rien

		if(this.ADN.nbneurones[0] >= 7){

			this.Pproche = this.calcProche(listeP);

			Poison = listeP[this.Pproche];

			this.nodeprochepoison = this.calccoordsnode(Poison);
		
			if(this.nodeprochepoison == "O"){
				this.ADN.neurones[0][5].valeur = -1;
				this.ADN.neurones[0][6].valeur = 1;
			} else {
				this.ADN.neurones[0][5].valeur = 1;
				this.ADN.neurones[0][6].valeur = -1;
			}
		}
		//distance poison plus proche

		if(this.ADN.nbneurones[0] >= 8){
			this.corpsnodepoison = this.calcrapportdist(Poison);

			if(this.corpsnodepoison == "N"){
				this.ADN.neurones[0][7].valeur = -1;
			} else {
				this.ADN.neurones[0][7].valeur = 1;
			}
		}
		// distance poison plus proche

		if(this.ADN.nbneurones[0] >= 9)this.ADN.neurones[0][8].valeur = calcmoydist(dist(this.coords.x,this.coords.y,Poison.x,Poison.y));

		// print(this.ADN.neurones[0][0].valeur);
		// print(this.ADN.neurones[0][1].valeur,this.ADN.neurones[0][2].valeur);
		// print(this.ADN.neurones[0][3].valeur);
		// print(this.ADN.neurones[0][4].valeur);
		// print(this.ADN.neurones[0][4].valeur,this.ADN.neurones[0][5].valeur);
		// print(this.ADN.neurones[0][5].valeur);
	}

	calccachés(){
		// print(this.ADN.neurones)
		for(let i = 1; i < this.ADN.neurones.length;i++){ // pour chaques neurones par lignes 
			for(let j = 0; j < this.ADN.neurones[i].length;j++){// pour chaques neurones par colones
				for(let k = 0; k < this.ADN.neurones[i - 1].length;k++){ // pour chaque neurones ajoute sa valeur fois sa puissance
					this.ADN.neurones[i][j].valeur += this.ADN.neurones[i - 1][k].valeur * this.ADN.neurones[i - 1][k].connections[j];
				}
				this.ADN.neurones[i][j].valeur = calce(this.ADN.neurones[i][j].valeur);
			}
		}
	}

	calcphysique(){
		this.acc.limit(this.accmax);

		this.vitesse.add(this.acc);
		this.vitesse.limit(this.vitessemax);

		this.coords.add(this.vitesse);
		this.acc.setMag(0);

		this.calccolisions();
	}

	calcstamina(listeB,listeP){

		this.Bproche = this.calcProche(listeB);
		this.Pproche = this.calcProche(listeP);

		this.calcsurPoint(listeB,this.Bproche,1);
		this.calcsurPoint(listeP,this.Pproche,-1);

		this.stamina = this.stamina
		- (abs(this.ADN.neurones[this.ADN.neurones.length - 1][0].valeur / 5)
		+ abs(this.ADN.neurones[this.ADN.neurones.length - 1][1].valeur / 2)
		+ abs(this.ADN.neurones[this.ADN.neurones.length - 1][2].valeur / 5));

		if(this.stamina > this.staminamax){
			this.staminamax = this.stamina; 
		}
	}

	calcProche(liste){
		let temp;
		temp = 0;
		try{
			for(let i = 0; i < liste.length;i++){
				if(dist2(this.coords.x,this.coords.y,liste[i].x,liste[i].y) < dist2(this.coords.x,this.coords.y,liste[temp].x,liste[temp].y)){
					temp = i;
				}
			}
			return temp;
		}
		catch(e){
			print("fuuuccckkkkk");
			print(e);
			print(liste.length,temp);
		}
	}

	calcsurPoint(liste,proche,coef){
		if(dist2(this.coords.x,this.coords.y,liste[proche].x,liste[proche].y) < 100){
			suprimerpoint(liste[proche]);
			this.stamina += 250 * coef;
		}
	}

	calcFitness(){
		// this.fitness = this.staminamax;
		// this.fitness = this.staminamax*(5 * this.nbboufemangé - 5 * this.nbpoisonmangé);
		// this.fitness = this.staminamax + 5 * this.nbboufemangé - 5 * this.nbpoisonmangé;
		// this.fitness = this.tmpsdevie * this.staminamax + 5 * this.nbboufemangé - 10 * this.nbpoisonmangé;
		// print(this.fitness)
		return this.staminamax
	}

	calccoordsnode(point){
		let xécartnode = cos(this.or + HALF_PI);
		let yécartnode = sin(this.or + HALF_PI);

		let xtotalgauche = this.coords.x + xécartnode;
		let ytotalgauche = this.coords.y + yécartnode;

		let xtotaldroite = this.coords.x - xécartnode;
		let ytotaldroite = this.coords.y - yécartnode;

		if(dist2(point.x,point.y,xtotalgauche,ytotalgauche) < dist2(point.x,point.y,xtotaldroite,ytotaldroite)){
			return "O"
		} else {
			return "E"
		}
	}

	calcrapportdist(point){
		let x1taillenavette = this.coords.x + cos(this.or) * taillenavette * -1; // le *-1 sert a avoir l'arrière du corps
		let y1taillenavette = this.coords.y + sin(this.or) * taillenavette * -1;
		let x2taillenavette = this.coords.x + cos(this.or) * taillenavette; // le *-1 sert a avoir l'arrière du corps
		let y2taillenavette = this.coords.y + sin(this.or) * taillenavette;

		if(dist2(point.x,point.y,x2taillenavette,y2taillenavette) < dist2(point.x,point.y,x1taillenavette,y1taillenavette)){
			return "N"
		} else {
			return "S"
		}
	}

	show(afficherproche){

		fill(this.couleur[0],this.couleur[1],this.couleur[2])

		if(afficherproche == true){
			try{
				ellipse(this.temp[0].x,this.temp[0].y,10)
				ellipse(this.temp[1].x,this.temp[1].y,10)
			}
			catch(e){
				print(temp)
			}
		}

		push();
		translate(this.coords.x,this.coords.y);
		rotate(this.or + PI / 2);

		// triangle(0,0,(cos(this.or+taillebase)*taillenavette),(sin(this.or+taillebase)*taillenavette),(cos(this.or-taillebase)*taillenavette),(sin(this.or-taillebase)*taillenavette));

		beginShape();
		vertex(-taillebase, 0);
		vertex(0, -taillenavette);
		vertex(taillebase, 0);
		vertex(0, taillenavette);
		endShape(CLOSE);

		//triangle(0,0,-taillebase,-taillenavette,taillebase,-taillenavette);

		if(affichenode == true){ // on affiche les nodes
			
			line(0,0,écartnode*2,0);
			line(0,0,-écartnode*2,0);
			line(0,0,0,écartnode*2);
			line(0,0,0,-écartnode*2);

			let r1,r2,g1,g2;

			if(this.nodeprocheboufe == "O"){
				r1 = 255;
				r2 = 0;
			} else{
				r1 = 0;
				r2 = 255;
			}

			if(this.nodeprochepoison == "O"){
				g1 = 255;
				g2 = 0;
			} else{
				g1 = 0;
				g2 = 255;
			}

			fill(r1,g1,0);
			ellipse(-écartnode*2,0,5);
			fill(r2,g2,0);
			ellipse(écartnode*2,0,5);

			if(this.corpsnodeboufe == "O"){
				r1 = 255;
				r2 = 0;
			} else{
				r1 = 0;
				r2 = 255;
			}

			if(this.corpsnodepoison == "O"){
				g1 = 255;
				g2 = 0;
			} else{
				g1 = 0;
				g2 = 255;
			}

			fill(r1,g1,0);
			ellipse(0,-écartnode*2,5);
			fill(r2,g2,0);
			ellipse(0,écartnode*2,5);
		}

		pop();
	}
}

class Pt{
	constructor(){
		this.x = random(TX);
		this.y = random(TY);
		this.r = 5;
	}

	show(couleur){
		fill(couleurpopu[couleur][0],couleurpopu[couleur][1],couleurpopu[couleur][2]);
		ellipse(this.x,this.y,this.r);
	}
}