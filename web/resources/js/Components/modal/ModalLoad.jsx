import React from 'react'
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import { CopyBlock, dracula } from 'react-code-blocks';
import { ExtractHuggingFaceId } from '@/utils';

const ModalLoad = (props) => {
    const function_str = props.dataset ? "load_dataset" : "load_model"
    const resource_str = ExtractHuggingFaceId(props.dataset.link.hugging_face_url ?? props.model.link.hugging_face_url)

    const code_str =
        `
    from pt_pump_up import PTPumpUpClient
    
    client = PTPumpUpClient()
    
    elem = client.${function_str}(${resource_str})
    `

    return (
        <Modal open={props.open} onClose={props.handleClose}>
            <Box className="modal">
                <CopyBlock className="code-block" text={code_str} language={"python"} theme={dracula} showLineNumbers={false} />
            </Box>
        </Modal>
    )
}

export default ModalLoad