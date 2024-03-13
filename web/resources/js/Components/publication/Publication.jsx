import React from 'react'
import Cite from 'citation-js'
import { ToProperCase, ExtractYearFromBibtex } from '@/utils';
import Grid from '@mui/material/Grid'
import CircleIcon from '@mui/icons-material/Circle';

const Publication = (props) => {

    const citation = new Cite(props.publication.bibtex).data[0]

    return (
        <Grid container direction="row" justifyContent="center" alignItems="center" sx={{ height: "100%" }}>
            <Grid container xs={1} sx={{ display: { xs: 'flex', lg: 'none' } }}>
                <CircleIcon className="circle-main-page" />
            </Grid>
            <Grid container xs={10} direction="column" justifyContent="center" alignItems="start" className="publication" sx={{ px: 3, py: 3 }}>
                <Grid item sx={{ mb: 3 }}>{ToProperCase(citation.title)}</Grid>
                <Grid item>Year: {ExtractYearFromBibtex(citation.id)}</Grid>
            </Grid>
        </Grid>
    )
}

export default Publication