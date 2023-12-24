import React from 'react'
import Grid from '@mui/material/Grid'
import { FormControl } from '@mui/material'
import TextField from '@mui/material/TextField'
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import Button from '@mui/material/Button'
import GenericDivider from '@/Components/GenericDivider'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Typography from '@mui/material/Typography'
import { router } from '@inertiajs/react'


const ShowResource = (props) => {

    return (
        <Grid container alignItems="center" justifyContent="center">
            <Grid container alignItems="center" justifyContent="space-between" sx={{ mb: 5 }}>
                <Grid item>
                    <h1>{props.elem.english_name}</h1>
                </Grid>
                {props.elem.href.link_papers_with_code &&
                    <Grid item>
                        <Button variant="contained" color="primary" href={props.elem.href.link_papers_with_code}>View in Papers With Code</Button>
                    </Grid>
                }
                {props.auth.user &&
                    <Grid item xs={"auto"}>
                        <Button variant="contained" color="error" onClick={() => router.delete(route(props.delete_route, props.elem.id), { replace: true })}>Delete Resource</Button>
                    </Grid>
                }
            </Grid>
            <Grid item xs={8}>
                <FormControl fullWidth sx={{ mb: 3 }}>
                    <h3>English Name</h3>
                    <TextField disabled value={props.elem.english_name} variant="outlined" />
                </FormControl>
            </Grid>
            <GenericDivider label="Authors" />
            <Grid container justifyContent="center" alignItems="center">
                {props.elem.authors.map((author, index) => (
                    <Card key={index}>
                        <CardContent>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                                {author.name}
                            </Typography>
                            <Typography variant="h5" component="div">
                                {author.href.email}
                            </Typography>
                        </CardContent>
                    </Card>
                ))}
            </Grid>
            {props.children}
        </Grid>
    )
}

export default ShowResource