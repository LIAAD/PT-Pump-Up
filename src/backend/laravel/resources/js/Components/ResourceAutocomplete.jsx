import React from 'react'
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card'
import CardHeader from '@mui/material/CardHeader'
import CloseIcon from '@mui/icons-material/Close'
import Autocomplete from '@mui/material/Autocomplete'
import TextField from '@mui/material/TextField'
import GenericDivider from '@/Components/GenericDivider'



const NewAutocomplete = (props) => {
    const renderFunction = (params) => {
        return (
            <TextField {...params} label={props.label} />
        )
    }
    return (
        <Autocomplete
            disablePortal
            options={props.options}
            renderInput={renderFunction}
        />
    )
}

const SelectedCard = (props) => {
    return (
        <Card>
            <CardHeader
                title={props.title}
                action={
                    <CloseIcon onClick={props.onClick} />
                }
            />

        </Card>
    )
}


const ResourceAutocomplete = (props) => {
    return (
        <>
            <GenericDivider label={props.label} />

            <Grid container alignItems="center" justifyContent="center">
                {props.stateElements.map((elem, index) => {
                    <Grid item xs={6}>
                        <SelectedCard title={elem} onClick={props.onClick} />
                    </Grid>
                })}
                <Grid item xs={6}>
                    <NewAutocomplete label={props.label} options={props.propsElements} />
                </Grid>
            </Grid>
        </>

    )
}

export default ResourceAutocomplete