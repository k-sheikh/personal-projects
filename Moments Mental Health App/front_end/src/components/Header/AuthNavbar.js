import logo from './../../static/logo_with_text.svg'
import { Link } from 'react-router-dom'
import Button from './../Button/Button'

const AuthNavbar = ({invalidateToken}) => {
    return (
        <div>
            <nav className="navBar">
            <Link to='/'><img className='logo left' src={logo} alt="Moments Logo"></img></Link>
            <div className="buttonsContainer">
                <Link to='/'>
                    <Button 
                        buttonStyle="btn--blue" 
                        text= "Home" 
                    /> 
                </Link> 
                <Link to='/browse-moments'>   
                    <Button 
                        buttonStyle="btn--blue" 
                        text= "Moments" 
                    /> 
                </Link> 
                <Link to='/browse-journal'>   
                    <Button 
                        buttonStyle="btn--blue" 
                        text= "Journal" 
                    /> 
                </Link>
                <Link to='/'>
                <Button
                buttonStyle="btn--blue"
                event={invalidateToken}
                text="Sign out"
                />
                </Link>   
            </div>
            </nav>
        </div>
    )
}

export default AuthNavbar
