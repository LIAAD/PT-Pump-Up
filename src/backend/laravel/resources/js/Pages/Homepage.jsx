import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React from 'react'
import Grid from '@mui/material/Grid'
import ListIcon from '@mui/icons-material/List';
import GenericDivider from '@/Components/GenericDivider';
import Publication from '@/Components/Publication';
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
            <img src={props.member.img} className="profile-img" />
            <h3>{props.member.name}</h3>
            <h4>{props.member.title}</h4>
            <h4>{props.member.affiliation}</h4>
            <Grid container alignItems="center" justifyContent="center" >
                <Grid item xs={4}>
                    <Button href={`mailto:${props.member.href.email}`} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <EmailIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>
                {props.member.href.linkedin && <Grid item xs={4}>
                    <Button href={props.member.href.linkedin} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <LinkedInIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
                {props.member.href.github && <Grid item xs={4}>
                    <Button href={props.member.href.github} className="blue-inesc" target="_blank" rel="noopener noreferrer">
                        <GitHubIcon sx={{ fontSize: 40 }} />
                    </Button>
                </Grid>}
            </Grid>
        </Grid>
    )
}

const Index = (props) => {

    const extract_publication = () => {
        let publications = []
        props.team.map((member) => {
            member.publications.map((publication) => {
                publications.push(new Cite(publication.doi ? publication.doi : publication.bibtex))
            })
        })
        return publications
    }


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
                        <FigureItem number={props.nlp_tasks} title="NLP Tasks" />
                    </Grid>
                    <GenericDivider label="Our Team" />
                    <Grid container alignItems="center" justifyContent="space-around">
                        {props.team.map((member, index) =>
                            <Profile key={index} member={member} />
                        )}
                    </Grid>
                    <GenericDivider label="Publications" />
                    <ul>
                        {extract_publication().map((publication, index) =>
                            <Publication key={index} publication={publication} />
                        )}
                    </ul>
                </Grid>
            }
        />
    )
}

export default Index