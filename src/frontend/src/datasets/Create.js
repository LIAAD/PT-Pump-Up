import React from 'react'
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Divider from '@mui/material/Divider';
import Chip from '@mui/material/Chip';


const Create = (props) => {

    const [state, setState] = useState({
        name: '',
        year: '',
        languages: []
    })

    useEffect(() => {
        axios.get('/api/languages').then((response) => {
            console.log(response.data)
        }).catch((error) => {
            if (!isCancel(error)) {
                console.log(error)
            }
        })
    }, [])

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log('submit')
    }


    return (
        <form onSubmit={handleSubmit}>
            <Grid container direction="column" justifyContent="center" alignItems="center" spacing={4}>
                <Divider><Chip label="General Information" /></Divider>
                <TextField
                    label="Name"
                    variant="outlined"
                    onChange={e => props.handleInputChange(e, setState)}
                    placeholder="HAREM"
                    margin="normal" />
                <TextField
                    label="Year"
                    type="number"
                    InputLabelProps={{ shrink: true }}
                    placeholder={2023}
                    margin="normal"
                />
                <Divider><Chip label="Languages" /></Divider>
            </Grid>
        </form>
    )
}

export default Create