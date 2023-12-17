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


const TableModel = (props) => {
  return (
    <Grid container>
      <Grid item xs={12}>
        <h2>{props.task}</h2>
      </Grid>
      <Grid item xs={12}>
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
          <TableBody>
            {props.models.map((model, index) =>
              <TableRow key={index}>
                <TableCell scope="row" className="resource-name">
                  {model.name}
                </TableCell>
                <TableCell scope="row" align="center">
                  {model.year}
                </TableCell>
                <TableCell scope="row" align="center">
                  <Button href={model.hrefs.link_source} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button>
                </TableCell>
                <TableCell scope="row" align="center">
                  {model.model_stats.standard_format ? <ClearIcon /> : <CheckIcon />}
                </TableCell>
                <TableCell scope="row" align="center">
                  {model.model_stats.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
                </TableCell>
                <TableCell scope="row" align="center" className={`label-${model.model_stats.preservation_rating}`}>
                  {model.model_stats.preservation_rating.replace(model.model_stats.preservation_rating[0], model.model_stats.preservation_rating[0].toUpperCase())}
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Grid>

    </Grid>
  )
}




const Index = (props) => {
  const [state, setState] = useState({
    models: [],
  })

  useEffect(() => {
    setState({ ...state, models: filterByNLPTask(props.ml_models) })
  })

  return (
    <PTPumpUpLayout
      main={
        <Grid container>
          <Grid item>
            <h2>Model Index</h2>
          </Grid>
          {Object.keys(state.models).map((key) =>
            <TableModel key={key} task={key} models={state.models[key]} />
          )}
        </Grid>
      }
    />
  )
}

export default Index