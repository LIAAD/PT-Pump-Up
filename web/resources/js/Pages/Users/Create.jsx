import React, { useState } from 'react'
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import Grid from '@mui/material/Grid'
import FormControl from '@mui/material/FormControl'
import TextField from '@mui/material/TextField'
import { handleChangeTextFields } from '@/utils'
import Button from '@mui/material/Button'
import { router, usePage } from '@inertiajs/react'
import FormHelperText from '@mui/material/FormHelperText'
import FormGroup from '@mui/material/FormGroup'
import FormControlLabel from '@mui/material/FormControlLabel'
import Checkbox from '@mui/material/Checkbox'


const Create = (props) => {

    const { errors } = usePage().props

    const [state, setState] = useState({
        saving: false,
        name: '',
        email: '',
        institution: '',
        linkedin: '',
        agree: false,
    })

    const handleSubmit = (e) => {
        e.preventDefault()

        setState({ ...state, saving: true })

        router.post(route('users.store'), { ...state },
            {
                onFinish: () => {
                    setState({ ...state, saving: false })
                },
            })
    }

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
                        <FormGroup>
                            <FormControlLabel
                                control={<Checkbox checked={state.agree} onChange={(e) => setState({ ...state, agree: e.target.checked })} />}
                                label="I accept my Name, Email, Institution and LinkedIn to be stored in our database for future contact."
                            />
                            <FormHelperText error>{errors.agree}</FormHelperText>
                        </FormGroup>
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