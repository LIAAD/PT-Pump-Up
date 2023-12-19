import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React, { useState } from 'react'
import { FormControl, FormHelperText } from '@mui/material'
import TextField from '@mui/material/TextField'
import Grid from '@mui/material/Grid'
import { handleTextFieldChange } from '@/utils'
import ResourceAutocomplete from '@/Components/ResourceAutocomplete'
import Button from '@mui/material/Button'
import { router } from '@inertiajs/react'
import GenericDivider from '@/Components/GenericDivider'
import { FormControlLabel, FormGroup, Switch } from '@mui/material'

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
        broken_link: false,
        author_response: false,
        standard_format: false,
        backup: false,
        off_the_shelf: false,
        submit: false,
        description: '',
    })

    const handleSubmit = (e) => {
        e.preventDefault()

        setState({ ...state, submit: true })

        router.post(route('datasets.store'), {
            english_name: state.english_name,
            portuguese_name: state.portuguese_name,
            year: state.year,
            hrefs: {
                link_source: state.source_url,
                link_huggingface: state.link_huggingface,
                doi: state.doi,
            },
            dataset_stats: {
                broken_link: state.broken_link == "on" ? true : false,
                author_response: state.author_response == "on" ? true : false,
                standard_format: state.standard_format == "on" ? true : false,
                backup: state.backup == "on" ? true : false,
                off_the_shelf: state.off_the_shelf == "on" ? true : false,
            },
            authors: state.authors.map(elem => elem.href.email),
            nlp_tasks: state.nlp_tasks.map(elem => elem.acronym),
            language_stats: state.languages.map(elem => elem.iso_code),
            description: state.description,
        }, {
            onerror: () => {
                setState({ ...state, submit: false })
            },
        })

    }


    const removeElement = (e, key, value) => setState({ ...state, [key]: state[key].filter(elem => elem.id !== value.id) })


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
                                <TextField label="Description" variant="outlined" required multiline rows={3} onChange={e => handleTextFieldChange(e, state, setState)} name="description" />
                                <FormHelperText>Description of dataset</FormHelperText>
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
                        <GenericDivider label="Stats" />

                        <Grid container justifyContent="center" alignItems="center">
                            <Grid xs={"auto"} item>
                                <FormGroup>
                                    <FormControlLabel required control={<Switch onChange={e => handleTextFieldChange(e, state, setState)} />} label="Broken Link" name="broken_link" />
                                    <FormControlLabel required control={<Switch onChange={e => handleTextFieldChange(e, state, setState)} />} label="Author Response" name="author_response" />
                                    <FormControlLabel required control={<Switch onChange={e => handleTextFieldChange(e, state, setState)} />} label="Standard Format" name="standard_format" />
                                    <FormControlLabel required control={<Switch onChange={e => handleTextFieldChange(e, state, setState)} />} label="Backup" name="backup" />
                                    <FormControlLabel required control={<Switch onChange={e => handleTextFieldChange(e, state, setState)} />} label="Off the Shelf" name="off_the_shelf" />
                                </FormGroup>
                            </Grid>

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

                        <Grid sx={{ mt: 5 }}>
                            {!state.submit && <Button variant="contained" onClick={handleSubmit}>Submit</Button>}
                        </Grid>
                    </Grid>

                </form >
            }
        />
    )
}

export default Create