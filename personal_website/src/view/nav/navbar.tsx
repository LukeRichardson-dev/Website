import React from "react";
import { Link } from "react-router-dom";
import AccountButton from "./account/account";
import './navbar.css';
import OptionsButton from "./options/options";

function NavBar() {
    return (
        <nav id='nav-bar'>
            <Link to='options' >
                <OptionsButton />
            </Link>
            <Link to='account'>
                <AccountButton />
            </Link>
        </nav>
    );
}

export default NavBar;