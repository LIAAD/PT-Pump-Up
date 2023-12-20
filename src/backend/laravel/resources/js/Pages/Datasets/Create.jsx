import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React, { useState } from 'react'
import { router } from '@inertiajs/react'
import FormAddResource from '@/Components/FormAddResource'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'

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
            onError: () => {
                setState({ ...state, submit: false })
            },
            onFinish: () => {
                setState({ ...state, submit: false })
            }
        })

    }

    return (
        <PTPumpUpLayout
            main={
                <FormAddResource
                    state={state}
                    setState={setState}
                    handleSubmit={handleSubmit}
                    resource="dataset"
                    datasets={props.datasets}
                    languages={props.languages}
                    authors={props.authors}
                    nlp_tasks={props.nlp_tasks}
                >
                    <Grid sx={{ mt: 5 }}>
                        {!state.submit && <Button variant="contained" onClick={handleSubmit}>Submit</Button>}
                    </Grid>
                </FormAddResource>
            }
        />
    )
}

export default Create