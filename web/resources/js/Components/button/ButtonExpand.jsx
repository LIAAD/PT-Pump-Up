import React from 'react'
import IconButton from '@mui/material/IconButton'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ExpandLessIcon from '@mui/icons-material/ExpandLess'

const ButtonExpand = (props) => {
    return (
        <>
            {!props.state.expanded &&
                <IconButton size="large" onClick={() => props.setState({ ...props.state, expanded: !props.state.expanded })}>
                    <ExpandMoreIcon fontSize="large" />
                </IconButton>
            }
            {props.state.expanded &&
                <IconButton size="large" onClick={() => props.setState({ ...props.state, expanded: !props.state.expanded })}>
                    <ExpandLessIcon fontSize="large" />
                </IconButton>
            }
        </>
    )
}
export default ButtonExpand