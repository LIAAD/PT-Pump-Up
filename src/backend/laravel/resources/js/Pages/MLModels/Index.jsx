import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React, { useState } from 'react'
import { useEffect } from 'react'
import Grid from '@mui/material/Grid'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import LinkIcon from '@mui/icons-material/Link';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';
import { filterByNLPTask } from '@/utils';
import AddIcon from '@mui/icons-material/Add';
import { router } from '@inertiajs/react'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import IconButton from '@mui/material/IconButton';


const TableContent = (props) => {
  return (
    <TableBody>
      {props.models.map((model, index) =>
        <TableRow hover={true} key={index} onClick={() => router.get(route('models.show', model.id))}>
          <TableCell scope="row" className="resource-name">
            {model.english_name}
          </TableCell>
          <TableCell scope="row" align="center">
            {model.year}
          </TableCell>
          <TableCell scope="row" align="center">
            <Button href={model.href.link_source} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button>
          </TableCell>
          <TableCell scope="row" align="center">
            {model.resource_stats.standard_format ? <ClearIcon /> : <CheckIcon />}
          </TableCell>
          <TableCell scope="row" align="center">
            {model.resource_stats.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
          </TableCell>
          <TableCell scope="row" align="center" className={`label-${model.resource_stats.preservation_rating}`}>
            {model.resource_stats.preservation_rating && model.resource_stats.preservation_rating.replace(model.resource_stats.preservation_rating[0], model.resource_stats.preservation_rating[0].toUpperCase())}
          </TableCell>
        </TableRow>
      )}
    </TableBody>
  );
}


const ColapsibleTable = (props) => {
  const [state, setState] = useState({
    expanded: props.expanded,
  })

  return (
    <Grid container justifyContent="center">
      <Grid item xs={11}>
        <h2>{props.task}</h2>
      </Grid>
      <Grid item>
        {!state.expanded &&
          <IconButton size="large" onClick={() => setState({ ...state, expanded: !state.expanded })}>
            <ExpandMoreIcon fontSize="large" />
          </IconButton>
        }
        {state.expanded &&
          <IconButton size="large" onClick={() => setState({ ...state, expanded: !state.expanded })}>
            <ExpandLessIcon fontSize="large" />
          </IconButton>
        }
      </Grid>
      <Grid item xs={11}>
        <Table stickyHeader className="table-resource">
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell align="center">Year</TableCell>
              <TableCell align="center">Source URL</TableCell>
              <TableCell align="center">Standardized</TableCell>
              <TableCell align="center">Off the Shelf</TableCell>
              <TableCell align="center">Preservation Rating</TableCell>
            </TableRow>
          </TableHead>
          {state.expanded && <TableContent models={props.models} />}
        </Table>
      </Grid>
    </Grid >
  )
}


const Index = (props) => {
  const [state, setState] = useState({
    models: [],
  })

  useEffect(() => {
    setState({ ...state, models: filterByNLPTask(props.ml_models) })
  }, [])

  return (
    <PTPumpUpLayout
      main={
        <Grid container>
          <Grid container alignItems="center">
            <Grid item>
              <h2>Model Index</h2>
            </Grid>
            {props.auth.user &&
              <Grid item sx={{ ml: "auto" }}>
                <Button variant="contained" href={route("models.create")}>Add New Model <AddIcon /> </Button>
              </Grid>
            }
          </Grid>
          {Object.keys(state.models).map((key, index) =>
            <ColapsibleTable key={index} task={key} models={state.models[key]} expanded={index === 0} />
          )}
        </Grid>
      }
    />
  )
}

export default Index