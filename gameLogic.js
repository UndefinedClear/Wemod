const port = 5550;

let modes = ['normal'];

class Game {
	constructor(ip: string, mode = 'normal') {
		this.ip = ip;
		
		if (mode in modes) {
			this.mode = mode;
		}
		else {
			this.mode = modes[0] 
		}
		
		
	}
}


// var game = new Game(ip, 'normal');