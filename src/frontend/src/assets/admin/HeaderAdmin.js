import React from 'react'
import Grid from '@mui/material/Grid';
import inescLogo from '../images/INESCTEC.png'
import Button from '@mui/material/Button';
import MenuIcon from '@mui/icons-material/Menu';


const HeaderAdmin = (props) => {
    return (
        <Grid container alignItems="center">
            <Grid item xs={"auto"} sx={{ mr: 2 }}>
                <Button href="/" sx={{ p: 0 }}><img id={"logo"} src={inescLogo} /></Button>
            </Grid>
            <Grid item xs={"auto"} lg={6}>
                <h1><span className="blue-inesc">PT-Pump-Up:</span> <span id="small-title">Hub for Portuguese NLP Resources</span></h1>
            </Grid>
            <Grid item xs={"auto"} sx={{ ml: "auto" }}>
                <Button className="blue-inesc" onClick={props.toggleDrawer} sx={{p:2}}><MenuIcon/></Button>
            </Grid>
        </Grid>
    )
}

export default HeaderAdmin  