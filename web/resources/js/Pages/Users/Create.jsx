import React, { useState } from 'react'
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import Grid from '@mui/material/Grid'
import FormControl from '@mui/material/FormControl'
import TextField from '@mui/material/TextField'
import { handleChangeTextFields } from '@/utils'
import Button from '@mui/material/Button'
import { router, usePage } from '@inertiajs/react'
import FormHelperText from '@mui/material/FormHelperText'


const Create = (props) => {

    const { errors } = usePage().props

    const [state, setState] = useState({
        saving: false,
        name: '',
        email: '',
        institution: '',
        linkedin: '',
    })

    const handleSubmit = (e) => {
        e.preventDefault()

        console.log(state)

        setState({ ...state, saving: true })

        router.post(route('users.store'), {
            name: state.name,
            email: state.email,
            institution: state.institution,
            linkedin: state.linkedin,
        },
            {
                onFinish: () => {
                    setState({ ...state, saving: false })
                },
            })
    }

    console.log(errors);

    return (
        <PTPumpUpLayout
            main={
                <Grid container justifyContent="center" alignItems="center" spacing={8} sx={{ mt: 5 }}>
                    <Grid item xs={12} md={8} sx={{ textAlign: "center" }}>
                        <h1>Join the Community</h1>
                        <p>Fill in the form below to join the community and contribute to the project.</p>
                    </Grid>
                    <Grid item xs={12} md={8}>
                        <FormControl fullWidth>
                            <TextField label="Your Name" variant="outlined" name="name" required onChange={(e) => handleChangeTextFields(e, state, setState)} />
                            <FormHelperText error>{errors.name}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} md={8}>
                        <FormControl fullWidth>
                            <TextField
                                label="Your Email"
                                variant="outlined"
                                name="email"
                                required
                                error={errors.email}
                                onChange={(e) => handleChangeTextFields(e, state, setState)} />
                            <FormHelperText error>{errors.email}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} md={8}>
                        <FormControl fullWidth>
                            <TextField
                                label="Your Institution"
                                variant="outlined"
                                name="institution"
                                required
                                error={errors.institution}
                                onChange={(e) => handleChangeTextFields(e, state, setState)} />
                            <FormHelperText error>{errors.institution}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} md={8}>
                        <FormControl fullWidth>
                            <TextField
                                label="Your LinkedIn"
                                variant="outlined"
                                name="linkedin"
                                error={errors.linkedin}
                                onChange={(e) => handleChangeTextFields(e, state, setState)} />
                            <FormHelperText error>{errors.linkedin}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} md={8} sx={{ textAlign: "center" }}>
                        {!state.saving && <Button variant="contained" color="primary" size="large" sx={{ mt: 5 }} onClick={handleSubmit}>
                            Submit
                        </Button>}
                    </Grid>
                </Grid>
            }
        />
    )
}

export default Create