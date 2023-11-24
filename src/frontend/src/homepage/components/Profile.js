import React from 'react'
import Grid from '@mui/material/Grid';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import EmailIcon from '@mui/icons-material/Email';
import Button from '@mui/material/Button';
import GitHubIcon from '@mui/icons-material/GitHub';

// TODO: Add LinkedIn links
const Profile = (props) => {
    return (
        <Grid item xs={6} md={2} xl={1.5} sx={{ textAlign: "center", mr: 3 }} >
            <img src={props.member.img} className="profile-img" />
            <h3>{props.member.name}</h3>
            <h4>{props.member.title}</h4>
            <h4>{props.member.affiliation}</h4>
            <Grid container justifyContent="center" alignItems="center" >
                <Grid item xs={4}>
                    <Button href={`mailto:${props.member.email}`} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <EmailIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>
                {props.member.linkedin && <Grid item xs={4}>
                    <Button href={props.member.linkedin} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <LinkedInIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
                {props.member.github && <Grid item xs={4}>
                    <Button href={props.member.github} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <GitHubIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
            </Grid>
        </Grid>
    )
}

export default Profile