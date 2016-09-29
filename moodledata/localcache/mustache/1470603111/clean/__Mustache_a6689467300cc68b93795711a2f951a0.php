<?php

class __Mustache_a6689467300cc68b93795711a2f951a0 extends Mustache_Template
{
    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $buffer = '';
        $newContext = array();

        $value = $this->resolveValue($context->find('fromname'), $context);
        $buffer .= $indent . $value;
        $buffer .= '
';

        return $buffer;
    }
}
