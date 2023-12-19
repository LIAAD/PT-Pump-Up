import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React, { useState } from 'react'
import Grid from '@mui/material/Grid'
import BenchmarkAutocomplete from '@/Components/BenchmarkAutocomplete'
import FormAddResource from '@/Components/FormAddResource'
import { router } from '@inertiajs/react'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardHeader from '@mui/material/CardHeader'
import Button from '@mui/material/Button'
import CloseIcon from '@mui/icons-material/Close';



const BenchmarkCard = (props) => {

  return (
    <Grid item xs={6}>
      <Card>
        <CardHeader title={`Benchmark ${props.elem.id}`} action={
          <Button onClick={(e) => props.removeElement(e, props.elem.id)}><CloseIcon /></Button>
        } />
        <CardContent>
          <Grid container sx={{ mb: 3 }}>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              Train Dataset
            </Grid>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              {props.elem.train_dataset.english_name}
            </Grid>
          </Grid>
          <Grid container sx={{ mb: 3 }}>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              Validation Dataset
            </Grid>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              {props.elem.validation_dataset.english_name}
            </Grid>
          </Grid>
          <Grid container sx={{ mb: 3 }}>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              Test Dataset
            </Grid>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              {props.elem.test_dataset.english_name}
            </Grid>
          </Grid>
          <Grid container>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              {props.elem.metric}
            </Grid>
            <Grid item xs={6} sx={{ textAlign: "center" }}>
              {props.elem.performance}
            </Grid>
          </Grid>
        </CardContent>
      </Card>
    </Grid>
  )
}


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
    architecture: '',
    description: '',
    benchmarks: [],
  })

  const removeElement = (e, id) => {
    e.preventDefault()
    setState({
      ...state,
      benchmarks: state.benchmarks.filter(elem => elem.id != id)
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    setState({ ...state, submit: true })

    router.post(route('datasets.store_web'), {
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

  return (
    <PTPumpUpLayout
      main={
        <FormAddResource
          state={state}
          setState={setState}
          handleSubmit={handleSubmit}
          resource="model"
        >
          <Grid container justifyContent="center" alignItems="center">
            <BenchmarkAutocomplete datasets={props.datasets} state={state} setState={setState} />
          </Grid>
          <Grid container justifyContent="center" alignItems="center" sx={{ mt: 5 }}>
            {state.benchmarks.map((elem, index) => <BenchmarkCard key={index} elem={elem} removeElement={removeElement} />)}
          </Grid>
        </FormAddResource>
      }
    />
  )
}

export default Create