import inquirer from 'inquirer';
import { Scoring } from './Scoring.js';
import { Levels } from './Levels.js';

export class Game {

	constructor() {               							// Create properties of the game
		this.level = 0;										// Level variable start at 0
		this.score = new Scoring();							// Score variable of type Scoring.js
		this.dailyEvents = new Levels().listOfLevels;		// Create an empty array

		console.log('\nStart of a new day, lets go!\n');

		this.startGame();				// Start game
	}

	startGame() {
		/*this.dailyEvents.forEach(event => {
			inquirer.prompt({
				type: 'list',
				message: event.name,
				name: 'response',
				choices: event.actions.map((action, index) => action.name)
			})
			.then(({response}) => {
				console.log(response);
			});
		});*/

		const startLevel = () => {
			inquirer.prompt({
				type: 'list',
				message: `${this.dailyEvents[this.level].name}: what would you like to do?`,
				name: 'response',
				choices: this.dailyEvents[this.level].actions.map((action, index) => `${index + 1}: ${action.name}`)	// index + 1 to display from 1, not 0
			})

			.then(({response}) => {
				const responseData = response.split(': ');		// Seperate index from message

				switch(responseData[0]) {						// Switch to get index (message at 0)
					case '1': 
                    this.score.workScore += 3;
                    this.score.socialScore -= 2;
                    break;
                    case '2': 
                    this.score.workScore += 2;
                    this.score.socialScore -= 1;
                    break;
                    case '3': 
                    this.score.workScore -= 1;
                    this.score.socialScore += 2;
                    break;
                    case '4': 
                    this.score.workScore -= 2;
                    this.score.socialScore += 3;
                    break;
				}

				console.log(`${this.dailyEvents[this.level].actions[responseData[0] -1].message}\n`);		// index - 1 to correct earlier +1

				this.level++

				if(this.level < this.dailyEvents.length) {
					startLevel ();
				} else {
					// console.log(this.score.workScore);
                    // console.log(this.score.socialScore);
					console.log(this.score.calculateScores());
				}
			})
		}

		startLevel();
	}
}
