<?php

class __Mustache_efafb2b3d163aeb7704ba2b0b74fa2a9 extends Mustache_Template
{
    private $lambdaHelper;

    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $this->lambdaHelper = new Mustache_LambdaHelper($this->mustache, $context);
        $buffer = '';
        $newContext = array();

        // 'tagscount' section
        $value = $context->find('tagscount');
        $buffer .= $this->section6e0bc23bd570822a11cfe010a062accc($context, $indent, $value);

        return $buffer;
    }

    private function section35cd54248ef1a2a54527fd6114b87692(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'standardtag';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'standardtag';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section67d917c513e274c1292567be669478cc(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'numberofentries, blog, {{count}}';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'numberofentries, blog, ';
                $value = $this->resolveValue($context->find('count'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section21a2e97a3267964c0e1573f8a5842fd1(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'title="{{#str}}numberofentries, blog, {{count}}{{/str}}';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'title="';
                // 'str' section
                $value = $context->find('str');
                $buffer .= $this->section67d917c513e274c1292567be669478cc($context, $indent, $value);
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function sectionAfbed53d278baa88530f28f7a018cde3(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
                            <span class="flagged-tag">{{name}}</span></a>
                        ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '                            <span class="flagged-tag">';
                $value = $this->resolveValue($context->find('name'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '</span></a>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section899a3dc2b8fce9b331d85717d6f862da(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
            <li>
                <a href="{{viewurl}}" class="{{#isstandard}}standardtag{{/isstandard}} s{{size}}"
                    {{#count}}title="{{#str}}numberofentries, blog, {{count}}{{/str}}{{/count}}">
                        {{#flag}}
                            <span class="flagged-tag">{{name}}</span></a>
                        {{/flag}}
                        {{^flag}}
                            {{name}}</a>
                        {{/flag}}
            </li>
        ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '            <li>
';
                $buffer .= $indent . '                <a href="';
                $value = $this->resolveValue($context->find('viewurl'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '" class="';
                // 'isstandard' section
                $value = $context->find('isstandard');
                $buffer .= $this->section35cd54248ef1a2a54527fd6114b87692($context, $indent, $value);
                $buffer .= ' s';
                $value = $this->resolveValue($context->find('size'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '"
';
                $buffer .= $indent . '                    ';
                // 'count' section
                $value = $context->find('count');
                $buffer .= $this->section21a2e97a3267964c0e1573f8a5842fd1($context, $indent, $value);
                $buffer .= '">
';
                // 'flag' section
                $value = $context->find('flag');
                $buffer .= $this->sectionAfbed53d278baa88530f28f7a018cde3($context, $indent, $value);
                // 'flag' inverted section
                $value = $context->find('flag');
                if (empty($value)) {
                    
                    $buffer .= $indent . '                            ';
                    $value = $this->resolveValue($context->find('name'), $context);
                    $buffer .= call_user_func($this->mustache->getEscape(), $value);
                    $buffer .= '</a>
';
                }
                $buffer .= $indent . '            </li>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section67eebbdd04f100bc980e047ad113cf99(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = ' showingfirsttags, core_tag, {{tagscount}} ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= ' showingfirsttags, core_tag, ';
                $value = $this->resolveValue($context->find('tagscount'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= ' ';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section8c5d9b73fa62ebdad7f5b54c16e8126d(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
        <p class="tag_overflow">
            {{#str}} showingfirsttags, core_tag, {{tagscount}} {{/str}}
        </p>
    ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '        <p class="tag_overflow">
';
                $buffer .= $indent . '            ';
                // 'str' section
                $value = $context->find('str');
                $buffer .= $this->section67eebbdd04f100bc980e047ad113cf99($context, $indent, $value);
                $buffer .= '
';
                $buffer .= $indent . '        </p>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section6e0bc23bd570822a11cfe010a062accc(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
    <div class="tag_cloud">
    <ul class="inline-list">
        {{#tags}}
            <li>
                <a href="{{viewurl}}" class="{{#isstandard}}standardtag{{/isstandard}} s{{size}}"
                    {{#count}}title="{{#str}}numberofentries, blog, {{count}}{{/str}}{{/count}}">
                        {{#flag}}
                            <span class="flagged-tag">{{name}}</span></a>
                        {{/flag}}
                        {{^flag}}
                            {{name}}</a>
                        {{/flag}}
            </li>
        {{/tags}}
    </ul>
    {{#overflow}}
        <p class="tag_overflow">
            {{#str}} showingfirsttags, core_tag, {{tagscount}} {{/str}}
        </p>
    {{/overflow}}
    </div>
';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '    <div class="tag_cloud">
';
                $buffer .= $indent . '    <ul class="inline-list">
';
                // 'tags' section
                $value = $context->find('tags');
                $buffer .= $this->section899a3dc2b8fce9b331d85717d6f862da($context, $indent, $value);
                $buffer .= $indent . '    </ul>
';
                // 'overflow' section
                $value = $context->find('overflow');
                $buffer .= $this->section8c5d9b73fa62ebdad7f5b54c16e8126d($context, $indent, $value);
                $buffer .= $indent . '    </div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

}
