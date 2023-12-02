import React from 'react'
import { useState, useEffect } from 'react'
import LayoutAdmin from '../assets/admin/LayoutAdmin'
import Grid from '@mui/material/Grid';
import ListIcon from '@mui/icons-material/List';
import Divider from '@mui/material/Divider';
import Chip from '@mui/material/Chip';
import { sendGetRequest } from '../utils/requests';
import { filterByNLPTask } from '../utils/filterNLPTask';
import InescDivider from './components/InescDivider';
import Profile from './components/Profile';
import Cite from "citation-js";
import Publication from './components/Publication';

require("@citation-js/plugin-bibtex");

const Homepage = (props) => {

    const team = [
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
    ]

    const [state, setState] = useState({
        datasets: [],
        models: [],
        authors: [],
        publications: []
    })



    useEffect(() => {
        sendGetRequest('/api/homepage/').then((response) => {

            for (const key in response)
                response[key] = JSON.parse(response[key])

            const datasetsFiltered = filterByNLPTask(response.datasets)
            const modelsFiltered = filterByNLPTask(response.models)
            const publications = response.publications.map((publication) => new Cite(publication.doi ? publication.doi : publication.bibtex))

            setState({
                datasets: response.datasets,
                models: response.models,
                authors: response.authors,
                nlp_tasks: Math.max(Object.keys(datasetsFiltered).length, Object.keys(modelsFiltered).length),
                publications: publications
            })
        })
    }, [])

    return (
        <LayoutAdmin
            main={
                <Grid container className="force-padding">
                    <Grid container sx={{ mt: 5 }} justifyContent="center" alignItems="center">
                        <Grid item md={8}>
                            <h1>Sincronizing & Extending <br /> Portuguese NLP Resources</h1>
                        </Grid>
                        <Grid item md={2} sx={{ display: { xs: 'none', md: 'block' } }} >
                            <ListIcon sx={{ fontSize: 200 }} />
                        </Grid>
                    </Grid>
                    <InescDivider label="What is PT-Pump-Up?" />
                    <Grid item xs={12} sx={{ mx: 5 }}>
                        <h3>PT-Pump-Up is a hub for Portuguese NLP resources, which aims to provide a centralized access point to the most relevant resources for Portuguese NLP, as well as to provide a set of tools to facilitate their use.</h3>
                    </Grid>
                    <InescDivider label="Some Figures" />
                    <Grid container justifyContent="space-around" alignItems="center" >
                        <Grid item xs={12} md={3} lg={2} className='figure' >
                            <h3>{state.datasets.length}</h3>
                            <h4>Datasets</h4>
                        </Grid>
                        <Grid item xs={12} md={3} lg={2} className='figure' >
                            <h3>{state.models.length}</h3>
                            <h4>Models</h4>
                        </Grid>
                        <Grid item xs={12} md={3} lg={2} className='figure' >
                            <h3>{state.authors.length}</h3>
                            <h4>Authors</h4>
                        </Grid>
                        <Grid item xs={12} md={3} lg={2} className='figure' >
                            <h3>{state.nlp_tasks}</h3>
                            <h4>NLP Tasks</h4>
                        </Grid>
                    </Grid>
                    <InescDivider label="Our Team" />
                    <Grid container alignItems="center" justifyContent="space-around" >
                        {team.map((member, index) =>
                            <Profile key={index} member={member} />
                        )}
                    </Grid>
                    <InescDivider label="Publications" />
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

export default Homepage