import React from "react";
import { GrAppsRounded } from "react-icons/gr";
import './options.css';

class OptionsButton extends React.Component {
    render(): React.ReactNode {
        return (
            <div className='options-button'>
                <GrAppsRounded className="apps-icon" />
            </div>
        );
    }
}

export default OptionsButton;