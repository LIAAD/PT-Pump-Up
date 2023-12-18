import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React, { useState } from 'react'
import { FormControl, FormHelperText } from '@mui/material'
import TextField from '@mui/material/TextField'
import Grid from '@mui/material/Grid'
import { handleTextFieldChange } from '@/utils'
import ResourceAutocomplete from '@/Components/ResourceAutocomplete'

const Create = (props) => {

    const [state, setState] = useState({
        english_name: '',
        portuguese_name: '',
        year: '',
        source_url: '',
        link_huggingface: '',
        doi: '',
        authors: [],
        nlp_tasks: [],
        languages: [],
    })


    const removeElement = (e, key, value) => {
        setState({ ...state, [key]: state[key].filter(elem => elem.id !== value.id) })
    }


    return (
        <PTPumpUpLayout
            main={
                <form>
                    <Grid container sx={{ mt: 5 }} justifyContent="center" alignItems="center">
                        <Grid xs={8} item>
                            <FormControl fullWidth sx={{ mb: 3 }}>
                                <TextField label="English Name" variant="outlined" required onChange={e => handleTextFieldChange(e, state, setState)} name="english_name" />
                                <FormHelperText>English Name of the dataset</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid xs={8} item>
                            <FormControl fullWidth sx={{ mb: 3 }}>
                                <TextField label="Optional Portuguese Name" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="portuguese_name" />
                                <FormHelperText>A translation of the resource name to Portuguese</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid xs={8} item>

                            <FormControl fullWidth sx={{ mb: 3 }}>
                                <TextField label="Year" type="number" variant="outlined" required onChange={e => handleTextFieldChange(e, state, setState)} name="year" />
                                <FormHelperText>Year of publication</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid xs={8} item>
                            <FormControl fullWidth sx={{ mb: 3 }}>
                                <TextField label="Source URL" variant="outlined" required onChange={e => handleTextFieldChange(e, state, setState)} name="source_url" />
                                <FormHelperText>URL of the dataset</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid xs={8} item>
                            <FormControl fullWidth sx={{ mb: 3 }}>
                                <TextField label="Link HuggingFace" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="link_huggingface" />
                                <FormHelperText>URL of the dataset on HuggingFace</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid xs={8} item>
                            <FormControl fullWidth>
                                <TextField label="DOI" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="doi" />
                                <FormHelperText>DOI of the dataset</FormHelperText>
                            </FormControl>
                        </Grid>

                        <ResourceAutocomplete label="Languages" stateElements={state.languages} propsElements={props.languages} onChange={(e, newValue) => setState({ ...state, languages: [...state.languages, newValue] })} onDelete={
                            (e, value) => {
                                removeElement(e, 'languages', value)
                            }
                        } />

                        <ResourceAutocomplete label="Authors" stateElements={state.authors} propsElements={props.authors} onChange={(e, newValue) => setState({ ...state, authors: [...state.authors, newValue] })} onDelete={
                            (e, value) => {
                                removeElement(e, 'authors', value)
                            }
                        } />

                        <ResourceAutocomplete label="NLP Tasks" stateElements={state.nlp_tasks} propsElements={props.nlp_tasks} onChange={(e, newValue) => setState({ ...state, nlp_tasks: [...state.nlp_tasks, newValue] })}
                            onDelete={(e, value) => {
                                removeElement(e, 'nlp_tasks', value)
                            }}
                        />

                    </Grid>

                </form >
            }
        />
    )
}

export default Create