import { Level } from './Level.js';
import { Action } from './Action.js';

export class Levels {

    constructor() {

        this.listOfLevels = []

        this.populateListOfLevels()
    }

    populateListOfLevels() {

        const level1 = new Level('ALARM SOUNDS');
		level1.addAction(new Action('Already up doing some work', 'Great start to the day!'));
		level1.addAction(new Action('No snoozing today, lets go..', 'Ready to go..'));
        level1.addAction(new Action('Up late chatting, need a snooze', 'Extra 15 min of sleep :)'));
        level1.addAction(new Action('Went out last night, need a good lie in', 'Extra 30 min of sleep :D'));
		this.listOfLevels.push(level1);		// Push selection into listOfLevels array

		const level2 = new Level('BREAKFAST TIME');
        level2.addAction(new Action('Work through breakfast', 'Very productive!'));
        level2.addAction(new Action('Breakfast and coffee', 'Ready for the day'));
        level2.addAction(new Action('Gonna quickly meet a friend at the cafe', 'Running a tad late'));
        level2.addAction(new Action('Meeting a friend for a full english', 'Running very late'));
        this.listOfLevels.push(level2);

        const level3 = new Level('ARRIVE AT WORK');
        level3.addAction(new Action('Lets GO, no breaks required!', 'A whole lot of work done!'));
        level3.addAction(new Action('Got some work done, where\'s that coffee pot?', 'Good stuff'));
        level3.addAction(new Action('Birthday treats! lets congratulate them!', 'Sooo good, but now you\'re behind..'));
        level3.addAction(new Action('Got some drama going down in the emails, lets get involved!', 'Got no work done this morning :('));
        this.listOfLevels.push(level3);

        const level4 = new Level('LUNCHTIME');
        level4.addAction(new Action('Lunch is for wimps, lets work though it!', 'Feeling a little hungry but who cares!'));
        level4.addAction(new Action('Quick sandwich and back to work on time', 'Good stuff'));
        level4.addAction(new Action('Pub lunch with the team', 'Little late back to work :('));
        level4.addAction(new Action('Went to lunchtime bday drinks', 'Very late back to work & feeling very lazy..'));
        this.listOfLevels.push(level4);

        const level5 = new Level('AFTERNOON');
        level5.addAction(new Action('Head down, no stopping me!', 'A whole lot of work done!'));
        level5.addAction(new Action('Got some work done, another coffee anyone?', 'Good stuff'));
        level5.addAction(new Action('Just heard some juicy gossip, lets investigate', 'Dam, not very productive'));
        level5.addAction(new Action('Been chatting on emails all afternoon', 'Got absolutely no work done :('));
        this.listOfLevels.push(level5);

        const level6 = new Level('AFTER WORK');
        level6.addAction(new Action('Time for some overtime', 'A whole lot of work done!'));
        level6.addAction(new Action('Home time!', 'Off home I go ready for the next day!'));
        level6.addAction(new Action('Did someone day pub? im in..', 'Works done, time to unwind a bit..'));
        level6.addAction(new Action('Forget the pub, im going clubbing!', 'You will regret it tomorrow!'));
        this.listOfLevels.push(level6);
    }
}