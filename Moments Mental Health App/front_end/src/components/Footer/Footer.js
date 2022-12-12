import './Footer.css'
import { FaFacebookSquare,  FaInstagram, FaGithub, FaTwitter, FaEnvelope } from 'react-icons/fa'

const Footer = () => {
    return (
        <footer className="footer">
            <h1>
                <FaFacebookSquare style={{cursor:"pointer"}} />
            </h1>
            <h1>
            <FaInstagram style={{cursor:"pointer"}} />
            </h1>
            <h1>
                <FaTwitter style={{cursor:"pointer"}} />
            </h1>
            <h1>
                <FaEnvelope style={{cursor:"pointer"}} />
            </h1>
            <h1>
                <FaGithub style={{cursor:"pointer"}} />    
            </h1>
            <p>&#169; Copyright Moments 2021</p>
            {/* <p className="footer-text">&#169; Copyright Moments 2021</p> */}
        </footer>
    ) 
}

export default Footer