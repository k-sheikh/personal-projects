import { RiCloseCircleFill } from 'react-icons/ri'
import { Link } from 'react-router-dom'
import JournallingForm from "../components/JournalEntries/JournallingForm"

const GuidedJournalling = ({closeModal, prompts}) => {
    const promptObj = prompts[Math.floor((Math.random() * prompts.length))]
    const prompt = promptObj.prompt;
    return (
        <div>
            <Link to='/' className='text-link'>  
            <div className="closeModalIcon">
                <RiCloseCircleFill onClick={closeModal}/>
            </div>
            </Link>

            <div>
                <h3 className="modal-title">Guided Journalling</h3>
            </div>


            <div className="guided-prompt">
                <label>{prompt}</label>
            </div>

            <JournallingForm 
            id = {12490}
            prompt = {promptObj}
            />

           
        </div>
    )
}

export default GuidedJournalling
