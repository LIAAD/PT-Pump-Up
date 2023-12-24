import React from 'react'
import { FormControl, FormHelperText } from '@mui/material'
import TextField from '@mui/material/TextField'
import Grid from '@mui/material/Grid'
import { handleTextFieldChange } from '@/utils'
import ResourceAutocomplete from '@/Components/ResourceAutocomplete'
import GenericDivider from '@/Components/GenericDivider'
import { FormControlLabel, FormGroup, Switch } from '@mui/material'


const FormAddResource = (props) => {

  const [state, setState] = [props.state, props.setState]

  const removeElement = (e, key, value) => setState({ ...state, [key]: state[key].filter(elem => elem.id !== value.id) })

  return (
    <form>
      <Grid container sx={{ mt: 5 }} justifyContent="center" alignItems="center">
        <Grid xs={8} item>
          <FormControl fullWidth sx={{ mb: 3 }}>
            <TextField label="English Name" variant="outlined" required onChange={e => handleTextFieldChange(e, state, setState)} name="english_name" />
            <FormHelperText>English Name of the {props.resource}</FormHelperText>
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
            <FormHelperText>Description of {props.resource}</FormHelperText>
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
            <FormHelperText>URL of the {props.resource}</FormHelperText>
          </FormControl>
        </Grid>
        <Grid xs={8} item>
          <FormControl fullWidth sx={{ mb: 3 }}>
            <TextField label="Link HuggingFace" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="link_huggingface" />
            <FormHelperText>URL of the {props.resource} on HuggingFace</FormHelperText>
          </FormControl>
        </Grid>
        <Grid xs={8} item>
          <FormControl fullWidth sx={{ mb: 3 }}>
            <TextField label="Link Papers With Code" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="link_papers_with_code" />
            <FormHelperText>URL of the {props.resource} on Papers With Code</FormHelperText>
          </FormControl>
        </Grid>
        <Grid xs={8} item>
          <FormControl fullWidth>
            <TextField label="DOI" variant="outlined" onChange={e => handleTextFieldChange(e, state, setState)} name="doi" />
            <FormHelperText>DOI of the {props.resource}</FormHelperText>
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

        {props.languages && <ResourceAutocomplete label="Languages" stateElements={state.languages} propsElements={props.languages} onChange={(e, newValue) => setState({ ...state, languages: [...state.languages, newValue] })} onDelete={
          (e, value) => {
            removeElement(e, 'languages', value)
          }
        }
          optionLabel="name"
        />}

        <ResourceAutocomplete label="Authors" stateElements={state.authors} propsElements={props.authors} onChange={(e, newValue) => setState({ ...state, authors: [...state.authors, newValue] })} onDelete={
          (e, value) => {
            removeElement(e, 'authors', value)
          }
        } optionLabel="name"
        />

        <ResourceAutocomplete label="NLP Tasks" stateElements={state.nlp_tasks} propsElements={props.nlp_tasks} onChange={(e, newValue) => setState({ ...state, nlp_tasks: [...state.nlp_tasks, newValue] })}
          onDelete={(e, value) => {
            removeElement(e, 'nlp_tasks', value)
          }}
          optionLabel="acronym"
        />
        {props.children}
      </Grid >
    </form >
  )
}

export default FormAddResource