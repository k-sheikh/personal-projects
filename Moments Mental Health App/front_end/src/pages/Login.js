import Button from '../components/Button/Button'
import { Link } from 'react-router-dom'
import { RiCloseCircleFill } from 'react-icons/ri'
import PropTypes from 'prop-types'
import { useState } from 'react'
import './Modal.css'

// import SignUp from './SignUp'
// Modal.setAppElement('#root')

const Login = ({closeModal, LoginToSignupModalTransition, setToken}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    async function loginUser(credentials) {
        return fetch('/api/auth/login', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(credentials)
        })
        .then(data => data.json())
    }
    const handleSubmit = async e => {
        e.preventDefault();
        const token = await loginUser({
            username,
            password
        });
        if (!token['token']) {
            alert(token['username'] || token['password'])
        } else {
        setToken(token['token']);
        localStorage.setItem('moments_token', token['token'])
        }
    }
    return (
        <div>
            <Link to='/' className='text-link'>  
            <div className="closeModalIcon">
                <RiCloseCircleFill onClick={closeModal}/>
            </div>
            </Link>
            <div className="modal-heading">
                <h3>Welcome to Moments</h3>
            </div>

            <form onSubmit={handleSubmit}>
                <div>
                    <input className="modal-form" type="text" name="Username" placeholder="Please enter your username"
                    onChange={e => setUsername(e.target.value)}
                    ></input>
                </div>

                <div>
                    <input className="modal-form" type="password" name="Password" placeholder="Please enter your password"
                    onChange={e => setPassword(e.target.value)}
                    ></input>
                </div>
                <br/>
                <div className="formButton">
                <Button 
                buttonStyle="btn--red" 
                text= "Login" 
                value="Login"
                type="submit"
                />
                </div>
            </form>

            <div>
                <h3 className="modal-heading">Not signed up yet?</h3>
                <Link to='/sign-up' style={{textDecoration:"none"}}> 
                <div className="formButton">
                <Button 
                buttonStyle="btn--red" 
                text= "Sign up now!" 
                event= {LoginToSignupModalTransition}
                />
                </div>
                </Link>
            </div>
        </div>
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
  }
export default Login