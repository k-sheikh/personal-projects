import React, { useEffect, useState } from 'react'
import Modal from 'react-modal'


import Header from '../components/Header/Header'
import ImageTile from '../components/Image/ImageTile'
import ideas from '../static/ideas.svg'
import my_universe from '../static/my_universe.svg'
import AlternatingListHomePage from '../components/AlternatingLists/AlternatingListHomePage'

import FeatureList from '../components/FeaturesList/FeatureList'
import Button from '../components/Button/Button'
import Footer from '../components/Footer/Footer'

import Register from './Register'
import Login from './Login'
Modal.setAppElement('#root')

const HomePage = ({setToken}) => {
    
    useEffect(() => {
        async function loadUser() {
            const token = localStorage.getItem('moments_token')
            if (!token) return;
    
            const res = await fetch('/api/auth/account', {
                headers: {
                'Authorization': `token ${token}`
                },
            })
            const data = await res.json()
            if ('id' in data && 'username' in data) {
                setToken(token)
            }
        }
        
        loadUser()

    }, [setToken])

const customStyles = {
    content : {
        top: '50%',
        left: '50%',
        right: 'auto',
        bottom: 'auto',
        marginRight: '-50%',
        transform: 'translate(-50%, -50%)',
        borderRadius: '2rem'
    }
    };
const [registrationModalIsOpen,setRegistrationModalIsOpen]=useState(false)
const [loginModalIsOpen,setLoginModalIsOpen]=useState(false)
const openSignUpModal = () => {
    setRegistrationModalIsOpen(true)
}
const closeSignUpModal = () => {
    setRegistrationModalIsOpen(false)
}
const openLoginModal = () => {
    setLoginModalIsOpen(true)
}
const closeLoginModal = () => {
    setLoginModalIsOpen(false)
}
const LoginToSignupModalTransition = () => {
    setLoginModalIsOpen(false)
    setRegistrationModalIsOpen(true)
}
const SignupToLoginModalTransition = () => {
    setLoginModalIsOpen(true)
    setRegistrationModalIsOpen(false)
}
    return (
        <div>
            <Header 
            signUpModal={openSignUpModal}
            loginModal={openLoginModal}
            />
            <ImageTile
            image={ideas}
            title="Reflect with us"
            alt="Man with thought bubbles around him"
            />            
            <AlternatingListHomePage />
            <FeatureList />
            <div className="Section4">
                <ImageTile
                image={my_universe}
                title="Document your world"
                alt="Woman pointing at a globe"
                />
            </div>
            <div className="Section5">
                <h3>Ready to start journalling?</h3>
                {/* <Link to="/sign_up"> */}
                    <Button 
                    buttonStyle="btn--red" 
                    text= "Let's go!" 
                    event= {openSignUpModal}
                    />
                {/* </Link> */}
            </div>

            {/* Setting up modal for signing up */}
            <div className="modal">
            <Modal style={customStyles} isOpen={registrationModalIsOpen} onRequestClose={closeSignUpModal}>
                <Register 
                modalOpen = {registrationModalIsOpen}
                closeModal = {closeSignUpModal}
                SignupToLoginModalTransition = {SignupToLoginModalTransition}
                setToken = {setToken}
                />
            </Modal>
            </div>
            <div className="modal">
                <Modal style={customStyles} isOpen={loginModalIsOpen} onRequestClose={closeLoginModal}>
                <Login 
                setToken = {setToken}
                closeModal={closeLoginModal}
                LoginToSignupModalTransition={LoginToSignupModalTransition}
                />
                </Modal>
            </div>
            <Footer /> 

        </div>
    )
}

export default HomePage