import del from './../../static/Icon_Delete.svg'
import './icon.css'
const Icon = ({event}) => {
    const ElementStyle = {
        display: 'flex',
        border: 'none',
        backgroundColor: 'transparent',
        cursor: 'pointer',
        margin: 'auto',
        'font-size': '10px',
        padding: '5px',
        'margin-bottom': '-25px',
    }
    return (
        <button
        onClick={event}
        style={ElementStyle}
        >
        <img style={{width:'6em'}} src={del} alt="delete"/>
        </button>
    )
}

export default Icon
