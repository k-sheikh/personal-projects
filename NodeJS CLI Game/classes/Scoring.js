export class Scoring {

    constructor() {
        this.workScore = 0;
        this.socialScore = 0;
    }

    calculateScores() {
        if(this.workScore >= 0 && this.socialScore >= 0) {
            return 'You got a great work/life balance, keep it up!\n';
        } else if(this.workScore >= 0 && this.socialScore < -6) {
            return 'You work so hard, you might get a promotion, but nobody at work likes you, ' +
            'you might want to work on your social skills!\n';
        } else if(this.workScore >= 0 && this.socialScore < 0) {
            return 'You\'re doing well at work but you might want to be a bit more social\n';
        } else if(this.socialScore >= 0 && this.workScore < -6) {
            return 'You\'ve done no work and management have noticed, you might not have a job tomorrow!\n';
        } else if(this.socialScore >= 0 && this.workScore < 0) {
            return 'It\'s great to have fun at work, but dont let it affect your productivity\n';
        }
    }
}