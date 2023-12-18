import React from 'react'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'
import IconButton from '@mui/material/IconButton'
import MenuIcon from '@mui/icons-material/Menu'
import Box from '@mui/material/Box'
import inescLogo from '@/images/inesc-logo.png'


const GenericHeader = (props) => {
    return (
        <Grid container alignItems="center" sx={{ pb: { lg: 3 } }}>
            <Grid item xs={"auto"}>
                <Button>
                    <img src={inescLogo} />
                </Button>
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

export default GenericHeader