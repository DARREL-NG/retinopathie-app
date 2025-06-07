// tests/Upload.spec.js
import { mount } from '@vue/test-utils'
import Upload from '../frontend/src/components/Upload.vue'
import axios from 'axios'
jest.mock('axios')

describe('Upload.vue', () => {
  it('bouton désactivé sans fichier', () => {
    const w=mount(Upload)
    expect(w.find('button').attributes('disabled')).toBeDefined()
  })
  it('affiche le résultat', async () => {
    axios.post.mockResolvedValue({ data:{code:1,label:'DR'} })
    const w=mount(Upload)
    await w.setData({ file:new File([''], 'a.png') })
    await w.find('button').trigger('click')
    await w.vm.$nextTick()
    expect(w.text()).toContain('DR')
  })
})
