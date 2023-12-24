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
            getOptionLabel={(option) => option[props.optionLabel]}
            renderInput={renderFunction}
            onChange={(event, newValue) => { if (newValue) props.onChange(event, newValue) }}
        />
    )
}

const SelectedCard = (props) => {
    return (
        <Card>
            <CardHeader
                title={props.elem[props.optionLabel]}
                action={<CloseIcon onClick={props.onClick} />}
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
                <Grid item xs={6} >
                    <NewAutocomplete label={props.label} options={props.propsElements} onChange={props.onChange} optionLabel={props.optionLabel} />
                </Grid>
            </Grid>
            <Grid container alignItems="center" justifyContent="center">
                {props.stateElements.map((elem, index) =>
                    <Grid key={index} item xs={4} sx={{ mt: 5, mx: 2 }}>
                        <SelectedCard elem={elem} optionLabel={props.optionLabel} onClick={(e) => {
                            props.onDelete(e, elem)
                        }} />
                    </Grid>
                )}
            </Grid>
        </>
    )
}

export default ResourceAutocomplete