import React, { useState } from 'react'
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card'
import CardHeader from '@mui/material/CardHeader'
import Autocomplete from '@mui/material/Autocomplete'
import TextField from '@mui/material/TextField'
import GenericDivider from '@/Components/GenericDivider'
import CardContent from '@mui/material/CardContent'
import { FormControl, FormHelperText } from '@mui/material'
import { handleTextFieldChange } from '@/utils'
import AddIcon from '@mui/icons-material/Add';
import Button from '@mui/material/Button';


const NewAutocomplete = (props) => {

    const [state, setState] = useState({
        id: props.state.benchmarks.length + 1,
        train_dataset: '',
        validation_dataset: '',
        test_dataset: '',
        metric: '',
        performance: '',
    })

    const handleNewBenchmark = (e) => {
        e.preventDefault()

        props.setState({
            ...props.state,
            benchmarks: [...props.state.benchmarks, state]
        })


        setState({
            id: props.state.benchmarks.length + 1,
            train_dataset: '',
            validation_dataset: '',
            test_dataset: '',
            metric: '',
            performance: '',
        })
    }

    return (
        <Card>
            <CardHeader title={`Benchmark ${props.state.benchmarks.length + 1}`} action={
                <Button onClick={handleNewBenchmark}>Add Benchmark<AddIcon /></Button>
            } />
            <CardContent sx={{ pt: 3 }}>
                <Autocomplete
                    disablePortal
                    options={props.datasets}
                    getOptionLabel={(option) => option.english_name}
                    renderInput={(params) => <TextField {...params} label={"Train Dataset"} />}
                    onChange={(event, value) => setState({ ...state, train_dataset: value })}
                    sx={{ mb: 5 }}
                />
                <Autocomplete
                    disablePortal
                    options={props.datasets}
                    getOptionLabel={(option) => option.english_name}
                    renderInput={(params) => <TextField {...params} label={"Validation Dataset"} />}
                    onChange={(event, value) => setState({ ...state, validation_dataset: value })}
                    sx={{ mb: 5 }}
                />
                <Autocomplete
                    disablePortal
                    options={props.datasets}
                    getOptionLabel={(option) => option.english_name}
                    renderInput={(params) => <TextField {...params} label={"Test Dataset"} />}
                    onChange={(event, value) => setState({ ...state, test_dataset: value })}
                />
                <GenericDivider label="" />
                <FormControl fullWidth sx={{ mb: 3 }}>
                    <TextField label="Metric" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="metric" />
                    <FormHelperText>Metric of the dataset</FormHelperText>
                </FormControl>
                <FormControl fullWidth>
                    <TextField label="Performance" type="number" variant="outlined" required onChange={e => handleTextFieldChange(e, state, setState)} name="performance" />
                    <FormHelperText>Performance</FormHelperText>
                </FormControl>
            </CardContent>
        </Card>
    )
}

const BenchmarkAutocomplete = (props) => {
    return (
        <>
            <Grid item xs={12}>
                <GenericDivider label="Benchmarks" />
            </Grid>
            <Grid container alignItems="center" justifyContent="center">
                <Grid item xs={8}>
                    <NewAutocomplete {...props} label="Train Dataset" />
                </Grid>
            </Grid>
        </>
    )
}

export default BenchmarkAutocomplete