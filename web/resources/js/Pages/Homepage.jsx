import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React from 'react'
import Grid from '@mui/material/Grid'
import ListIcon from '@mui/icons-material/List';
import GenericDivider from '@/Components/divider/GenericDivider';
import Publication from '@/Components/publication/Publication';
import Button from '@mui/material/Button';
import EmailIcon from '@mui/icons-material/Email';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import GitHubIcon from '@mui/icons-material/GitHub';
import Cite from 'citation-js'



const FigureItem = (props) => {
    return (
        <Grid item xs={12} md={3} lg={2} className='figure'>
            <h3>{props.number}</h3>
            <h4>{props.title}</h4>
        </Grid>
    )
}

const Profile = (props) => {
    return (
        <Grid item xs={8} md={2} xl={1.5} sx={{ textAlign: "center", mb: { xs: 3 } }} >
            <img src={"/storage/"+ props.admin.photo.path} className="profile-img" />
            <h3>{props.admin.name}</h3>
            <h4>{props.admin.title}</h4>
            <h4>{props.admin.affiliation}</h4>
            <Grid container alignItems="center" justifyContent="center" >
                <Grid item xs={4}>
                    <Button href={`mailto:${props.admin.email}`} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <EmailIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>
                {props.admin.linkedin && <Grid item xs={4}>
                    <Button href={props.admin.linkedin} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <LinkedInIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
                {props.admin.github && <Grid item xs={4}>
                    <Button href={props.admin.github} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <GitHubIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
            </Grid>
        </Grid>
    )
}

const Index = (props) => {

    return (
        <PTPumpUpLayout
            main={
                <Grid container sx={{ px: { lg: 10 }, mt: { lg: 3 } }}>
                    <Grid container justifyContent="center" alignItems="center">
                        <Grid item xs={12} md={8} sx={{ textAlign: { xs: "center", md: "left" } }}>
                            <h1>Sincronizing & Extending <br /> Portuguese NLP Resources</h1>
                        </Grid>
                        <Grid item md={2} sx={{ display: { xs: 'none', md: 'block' } }} >
                            <ListIcon sx={{ fontSize: 200 }} />
                        </Grid>
                    </Grid>
                    <GenericDivider label="What is PT-Pump-Up?" />
                    <Grid item xs={12} sx={{ mx: { sm: 5 } }}>
                        <h3>PT-Pump-Up is a hub for Portuguese NLP resources, which aims to provide a centralized access point to the most relevant resources for Portuguese NLP, as well as to provide a set of tools to facilitate their use.</h3>
                    </Grid>
                    <GenericDivider label="Resources Avaiable?" />
                    <Grid container justifyContent="space-around" alignItems="center">
                        <FigureItem number={props.num_datasets} title="Datasets" />
                        <FigureItem number={props.num_models} title="Models" />
                        <FigureItem number={props.num_authors} title="Authors" />
                        <FigureItem number={props.num_nlp_tasks} title="NLP Tasks" />
                    </Grid>
                    <GenericDivider label="Our Team" />
                    <Grid container alignItems="center" justifyContent="space-around">
                        {props.admins.map((admin, index) =>
                            <Profile key={index} admin={admin} />
                        )}
                    </Grid>
                    <GenericDivider label="Publications" />
                    <ul>
                        {props.publications.map((publication, index) =>
                            <Publication key={index} publication={publication} />
                        )}
                    </ul>
                </Grid>
            }
        />
    )
}

export default Index