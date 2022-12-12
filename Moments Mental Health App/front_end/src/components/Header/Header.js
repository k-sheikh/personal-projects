import UnauthNavbar from './UnauthNavbar'
// import AuthNavbar from './AuthNavbar'
const Header = ({signUpModal, loginModal}) => {
    return (
        <div>
            {/* (userIsAuthorised ? <AuthNavbar /> : <UnauthNavbar />) */}
            <UnauthNavbar 
            signUpModal={signUpModal}
            loginModal={loginModal}
            />
        </div>
    )
}

export default Header