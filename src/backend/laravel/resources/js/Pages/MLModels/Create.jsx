import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import React from 'react'

const Create = (props) => {
  return (
    <PTPumpUpLayout main={
      <form>
        <FormControl>
          <InputLabel htmlFor="my-input">Email address</InputLabel>
          <Input id="my-input" aria-describedby="my-helper-text" />
          <FormHelperText id="my-helper-text">We'll never share your email.</FormHelperText>
        </FormControl>
      </form>
    } />
  )
}

export default Create