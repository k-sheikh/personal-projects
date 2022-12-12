import Button from '../components/Button/Button'
import { RiCloseCircleFill } from 'react-icons/ri'
import { Link } from 'react-router-dom'
import { useState } from 'react'

const Register = ({SignupToLoginModalTransition, closeModal, setToken}) => {

    const [username, setUsername] = useState()
    const [password, setPassword] = useState()
    const [confirmPassword, setConfirmPassword] = useState()
    const [email, setEmail] = useState()

    async function registerUser(credentials) {
        if (password !== confirmPassword){
            alert("Passwords don't match");
            return -1
    }   else {
        return fetch('/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(credentials)
        })
            .then(data => data.json())
    }
    }
    const handleSubmit = async e => {
        e.preventDefault();
        const token = await registerUser({
            username,
            password,
            email
        });
        if ((!token['token']) && (token['username'])) {
            alert(token['username'])
        } else if ((!token['token']) && (token['password'])){
            alert(token['password'])
        }
        else { setToken(token['token']) }
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
                    <input className="modal-form" type="text" name="Username" placeholder="Please enter a username"
                    onChange={e => setUsername(e.target.value)}
                    ></input>
                </div>
                <div>
                    <input className="modal-form" type="email" name="Email" placeholder="Please enter your email"
                    onChange={e => setEmail(e.target.value)}
                    ></input>
                </div>

                <div>
                    <input className="modal-form" type="password" name="Password" placeholder="Choose a password"
                    onChange={e => setPassword(e.target.value)}
                    ></input>
                </div>

                <div>
                    <input
                        className="modal-form"
                        type="password"
                        name="Confirm Password"
                        placeholder="Confirm Password"
                        onChange={e => setConfirmPassword(e.target.value)}
                    ></input>
                </div>
                <br/>
                <div className="formButton">                
                <Button 
                buttonStyle="btn--red" 
                type="submit"
                text= "Register" 
                value="Register"
                />
                </div>
            </form>
            <div>
                <h3 className="modal-heading">Already a member?</h3>
                
                <Link to='/login' style={{textDecoration:"none"}}>  
                <div className="formButton">
                <Button 
                buttonStyle="btn--red" 
                text= "Login here!" 
                event= {SignupToLoginModalTransition}
                />
                </div>
                </Link>
            </div>
        </div>
    )
    
}

export default Register


                    // <div>
                    //     <label>Reminder Frequency </label> 
                    // </div>
                    // <div>
                    //     <input type="checkbox"/> <span>None</span> 
                    //     <input type="checkbox"/> <span>Daily</span>
                    //     <input type="checkbox"/> <span>Weekly</span>
                    // </div> 