import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React from 'react'
import { useState } from 'react'
import Grid from '@mui/material/Grid'
import ListIcon from '@mui/icons-material/List';
import CustomDivider from '@/Components/CustomDivider';
import Publication from '@/Components/Publication';
import Button from '@mui/material/Button';
import EmailIcon from '@mui/icons-material/Email';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import GitHubIcon from '@mui/icons-material/GitHub';



const FigureItem = (props) => {
    return (
        <Grid item xs={12} md={3} lg={2} className='figure' >
            <h3>{props.number}</h3>
            <p>{props.title}</p>
        </Grid>
    )
}

const Profile = (props) => {
    return (
        <Grid item xs={6} md={2} xl={1.5} sx={{ textAlign: "center", mr: 3, mb: { xs: 3, md: 0 } }} >
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

const Index = (props) => {

    const [state, setState] = useState({
        team: [
            {
                'img': 'https://text2story.inesctec.pt/img/ruben_almeida.png',
                'name': 'Rúben Almeida',
                'title': 'NLP Researcher',
                'affiliation': 'INESC Tec',
                'linkedin': 'https://www.linkedin.com/in/almeida-ruben',
                'github': "https://github.com/arubenruben",
                "email": "ruben.f.almeida@inesctec.pt"
            },
            {
                'img': 'https://raw.githubusercontent.com/LIAAD/PT-Pump-Up/main/src/frontend/src/assets/images/RC5.png',
                'name': 'Ricardo Campos',
                'title': 'Coordinator',
                'affiliation': 'INESC Tec',
                "email": "ricardo.campos@inesctec.pt"
            },
            {
                'img': 'https://text2story.inesctec.pt/img/alipio.png',
                'name': 'Alípio Jorge',
                'title': 'Co-Coordinator',
                'affiliation': 'INESC Tec',
                "email": "amjorge@fc.up.pt"
            },
            {
                'img': 'https://text2story.inesctec.pt/img/sergio.jpg',
                'name': 'Sérgio Nunes',
                'title': 'Co-Coordinator',
                'affiliation': 'INESC Tec',
                "email": "ssn@fe.up.pt"
            }
        ],
        publications: [],
        authors: [],
        datasets: [],
        models: [],
        nlp_tasks: []
    })

    return (
        <PTPumpUpLayout
            main={
                <Grid container>
                    <Grid container justifyContent="center" alignItems="center">
                        <Grid item md={8}>
                            <h1>Sincronizing & Extending <br /> Portuguese NLP Resources</h1>
                        </Grid>
                        <Grid item md={2} sx={{ display: { xs: 'none', md: 'block' } }} >
                            <ListIcon sx={{ fontSize: 200 }} />
                        </Grid>
                    </Grid>
                    <CustomDivider label="What is PT-Pump-Up?" />
                    <Grid item xs={12} sx={{ mx: 5 }}>
                        <h3>PT-Pump-Up is a hub for Portuguese NLP resources, which aims to provide a centralized access point to the most relevant resources for Portuguese NLP, as well as to provide a set of tools to facilitate their use.</h3>
                    </Grid>
                    <CustomDivider label="What resources are available?" />
                    <Grid container justifyContent="space-around" alignItems="center">
                        <FigureItem number={state.datasets.length} title="Datasets" />
                        <FigureItem number={state.models.length} title="Models" />
                        <FigureItem number={state.authors.length} title="Authors" />
                        <FigureItem number={state.nlp_tasks.length} title="NLP Tasks" />
                    </Grid>
                    <CustomDivider label="Our Team" />
                    <Grid container alignItems="center" justifyContent="space-around">
                        {state.team.map((member, index) =>
                            <Profile key={index} member={member} />
                        )}
                    </Grid>
                    <CustomDivider label="Publications" />
                    <ul>
                        {state.publications.map((publication, index) =>
                            <Publication key={index} publication={publication} />
                        )}
                    </ul>
                </Grid>
            }
        />
    )
}

export default Index