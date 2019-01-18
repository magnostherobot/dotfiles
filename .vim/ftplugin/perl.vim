" set formatting executable to perltidy
" see :h formatprg
if (executable('perltidy'))
  setlocal formatexpr=''
  setlocal formatprg='perltidy'
endif
