import React, { ChangeEvent, FormEvent } from 'react';
import './signup.css';

interface SignupProps {}

interface SignupState {
    username: string,
    email: string,
    password: string,
}

class Signup extends React.Component<SignupProps, SignupState> {
    constructor(props: {}) {
        super(props);

        this.state = {
            username: '',
            email: '',
            password: '',
        }

        this.handleUsernameChange = this.handleUsernameChange.bind(this)
        this.handleEmailChange = this.handleEmailChange.bind(this)
        this.handlePasswordChange = this.handlePasswordChange.bind(this)
        this.signupSubmit = this.signupSubmit.bind(this)
    }

    signupSubmit(event: FormEvent) {
        alert(
            
        )

        event.preventDefault()
    }

    handleUsernameChange(event: React.FormEvent<HTMLInputElement>) {
        this.setState({
            username: event.currentTarget.value
        });
    }

    handleEmailChange(event: React.FormEvent<HTMLInputElement>) {
        this.setState({
            email: event.currentTarget.value
        });
    }

    handlePasswordChange(event: React.FormEvent<HTMLInputElement>) {
        this.setState({
            password: event.currentTarget.value ?? ''
        });
    }

    render(): React.ReactNode {
        return (
            <main className='signup-layout'>
                <form className='form-box' onSubmit={this.signupSubmit}>
                    <p>Username</p>
                    <input type='text' value={this.state.username} onChange={this.handleUsernameChange}/>
                    <p>Email</p>
                    <input type='text' value={this.state.email}  onChange={this.handleEmailChange}/>
                    <p>Password</p>
                    <input type='password' value={this.state.password}  onChange={this.handlePasswordChange}/>
                    <input type="submit" />
                </form>
            </main>
        );
    }
}

export default Signup;