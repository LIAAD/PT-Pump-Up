import React from 'react'
import Grid from '@mui/material/Grid';
import inescLogo from '../images/INESCTEC.png'
import Button from '@mui/material/Button';
import MenuIcon from '@mui/icons-material/Menu';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';


const HeaderAdmin = (props) => {
    return (
        <Grid container alignItems="center">
            <Grid item xs={"auto"} sx={{ mr: { xs: 0, md: 2 } }}>
                <Button href="/" sx={{ p: 0 }}><img id={"logo"} src={inescLogo} /></Button>
            </Grid>
            <Grid item xs={"auto"} lg={6}>
                <h1><span className="blue-inesc">PT-Pump-Up</span> <Box id="small-title" sx={{ display: { xs: 'none', md: 'inline' } }}>Hub for Portuguese NLP Resources</Box></h1>
            </Grid>
            <Grid item xs={1} sx={{ ml: "auto" }}>
                <IconButton className="blue-inesc" onClick={props.toggleDrawer} sx={{ p: 2 }} size="large"><MenuIcon fontSize="inherit" /></IconButton>
            </Grid>
        </Grid>
    )
}

export default HeaderAdmin  