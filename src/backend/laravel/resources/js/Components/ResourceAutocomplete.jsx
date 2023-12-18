import React, { useState } from 'react'
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
            getOptionLabel={(option) => option.name}
            renderInput={renderFunction}
            onChange={props.onChange}
        />
    )
}

const SelectedCard = (props) => {
    return (
        <Card>
            <CardHeader
                title={props.name}
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
            <Grid item xs={12}>
                <GenericDivider label={props.label} />
            </Grid>
            <Grid container alignItems="center" justifyContent="center">

                <Grid item xs={8} >
                    <NewAutocomplete label={props.label} options={props.propsElements} onChange={props.onChange} />
                </Grid>

                {props.stateElements.map((elem, index) => {
                    <Grid key={index} item xs={6}>
                        <SelectedCard title={elem} onClick={props.onClick} />
                    </Grid>
                })}
            </Grid>
        </>
    )
}

export default ResourceAutocomplete