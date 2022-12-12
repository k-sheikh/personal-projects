import { RiCloseCircleFill } from 'react-icons/ri'
import { Link} from 'react-router-dom'

import JournallingForm from "../components/JournalEntries/JournallingForm"

const Journalling = ({closeModal}) => {

    return (
        <div>
            
            <Link to='/' className='text-link'>  
            <div className="closeModalIcon">
                <RiCloseCircleFill onClick={closeModal}/>
            </div>
            </Link>

            <div>
                <h3 className="modal-title">Journalling</h3>
            </div>
            <JournallingForm 
            id = {12490}
            />

           
        </div>
    )
}

export default Journalling
